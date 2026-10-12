"use strict";
// Token Scanner — main thread (has access to the Figma document via `figma`).
//
// Scans color / number (corner radius, spacing & padding) / text-size values on the
// current page or the current selection, groups them by resolved value, reports which
// values are already bound to a variable/style and which are still raw, computes
// tokenization coverage, lets the user select matching nodes on the canvas, and applies
// an existing variable/style to a whole group ("merge").
//
// documentAccess is "dynamic-page" so every document lookup must use the async APIs.
// ----------------------------------------------------------------------------------
// Bootstrap
// ----------------------------------------------------------------------------------
figma.showUI(__html__, { width: 440, height: 680, themeColors: true });
// When we set the selection ourselves (the "select matching nodes" action) we record
// its signature here so the selection-driven auto-scan ignores that change instead of
// re-scoping the scan to those nodes.
let programmaticSelectionKey = null;
figma.ui.onmessage = (msg) => {
    switch (msg.type) {
        case 'scan':
            handleScanRequest();
            break;
        case 'select-nodes':
            void selectNodes(msg.nodeIds);
            break;
        case 'zoom-node':
            void selectNodes([msg.nodeId]);
            break;
        case 'apply-token':
            void applyToken(msg.occurrences, msg.target);
            break;
        case 'resize':
            figma.ui.resize(Math.max(320, Math.round(msg.width)), Math.max(400, Math.round(msg.height)));
            break;
        case 'close':
            figma.closePlugin();
            break;
    }
};
function selectionKey(nodes) {
    return nodes
        .map((n) => n.id)
        .sort()
        .join(',');
}
// The scope the scan runs against. It changes only when the *user* changes the selection;
// the plugin's own "select matching nodes" action deliberately does NOT re-scope the scan.
let scanScope = { kind: 'page' };
function captureScopeFromSelection() {
    const sel = figma.currentPage.selection;
    if (sel.length === 0) {
        scanScope = { kind: 'page' };
    }
    else {
        const name = sel.length > 1 ? sel[0].name + ' +' + (sel.length - 1) : sel[0].name;
        scanScope = { kind: 'selection', ids: sel.map((n) => n.id), name };
    }
}
function contextFromScope() {
    return scanScope.kind === 'page'
        ? { scope: 'page', contextName: figma.currentPage.name }
        : { scope: 'selection', contextName: scanScope.name };
}
// Scans are triggered manually by the user. Scope = current selection at that moment
// (whole page if nothing is selected), except when the selection is one the plugin set
// itself for the "select matching nodes" action — then the previous scope is kept.
function handleScanRequest() {
    const isOwnSelection = programmaticSelectionKey !== null && selectionKey(figma.currentPage.selection) === programmaticSelectionKey;
    if (!isOwnSelection)
        captureScopeFromSelection();
    void runScan();
}
// ----------------------------------------------------------------------------------
// Small helpers
// ----------------------------------------------------------------------------------
function clamp01(v) {
    return v < 0 ? 0 : v > 1 ? 1 : v;
}
function channelHex(c) {
    return Math.round(clamp01(c) * 255)
        .toString(16)
        .padStart(2, '0')
        .toUpperCase();
}
// 8-digit uppercase hex, used for grouping (opacity included).
function colorKey(color, opacity) {
    return '#' + channelHex(color.r) + channelHex(color.g) + channelHex(color.b) + channelHex(opacity);
}
// Human-friendly hex: drop the alpha byte when fully opaque.
function colorDisplay(hex8) {
    return hex8.slice(7) === 'FF' ? hex8.slice(0, 7) : hex8;
}
// A rounded number label so 12 and 12.0000001 don't split into two groups.
function numKey(n) {
    return Math.round(n * 100) / 100;
}
const varCache = new Map();
const styleCache = new Map();
async function resolveVariable(id) {
    if (varCache.has(id))
        return varCache.get(id);
    let info = null;
    try {
        const v = await figma.variables.getVariableByIdAsync(id);
        if (v)
            info = { name: v.name, remote: v.remote };
    }
    catch (_e) {
        info = null;
    }
    varCache.set(id, info);
    return info;
}
async function resolveStyle(id) {
    if (styleCache.has(id))
        return styleCache.get(id);
    let info = null;
    try {
        const s = await figma.getStyleByIdAsync(id);
        if (s)
            info = { name: s.name, remote: s.remote };
    }
    catch (_e) {
        info = null;
    }
    styleCache.set(id, info);
    return info;
}
async function variableBinding(alias) {
    const info = await resolveVariable(alias.id);
    return { type: 'variable', tokenId: alias.id, tokenName: info ? info.name : 'Variable', remote: info ? info.remote : false };
}
async function styleBinding(id) {
    const info = await resolveStyle(id);
    return { type: 'style', tokenId: id, tokenName: info ? info.name : 'Style', remote: info ? info.remote : false };
}
// Returns a usable style id, or null when empty / mixed.
function readStyleId(value) {
    if (value === figma.mixed)
        return null;
    return value ? value : null;
}
// ----------------------------------------------------------------------------------
// Node collection
// ----------------------------------------------------------------------------------
const SCAN_TYPES = [
    'RECTANGLE',
    'ELLIPSE',
    'POLYGON',
    'STAR',
    'VECTOR',
    'LINE',
    'TEXT',
    'FRAME',
    'COMPONENT',
    'COMPONENT_SET',
    'INSTANCE',
    'BOOLEAN_OPERATION',
    'SECTION',
];
async function collectScopeNodes() {
    if (scanScope.kind === 'page') {
        return figma.currentPage.findAllWithCriteria({ types: SCAN_TYPES });
    }
    const seen = new Set();
    const out = [];
    const add = (node) => {
        if (!seen.has(node.id)) {
            seen.add(node.id);
            out.push(node);
        }
    };
    for (const id of scanScope.ids) {
        const node = await figma.getNodeByIdAsync(id);
        if (!node || node.type === 'PAGE' || node.type === 'DOCUMENT')
            continue; // scope root may have been deleted
        const sn = node;
        if (SCAN_TYPES.indexOf(sn.type) !== -1)
            add(sn);
        if ('findAllWithCriteria' in sn) {
            for (const child of sn.findAllWithCriteria({ types: SCAN_TYPES }))
                add(child);
        }
    }
    return out;
}
// ----------------------------------------------------------------------------------
// Value extraction
// ----------------------------------------------------------------------------------
function isSolidPaint(paint) {
    return paint.type === 'SOLID';
}
async function paintBinding(paint, styleId) {
    const bound = paint.boundVariables && paint.boundVariables.color;
    if (bound)
        return variableBinding(bound);
    if (styleId)
        return styleBinding(styleId);
    return { type: 'none' };
}
async function extractColors(node, occ) {
    // Fills
    if ('fills' in node && node.fills !== figma.mixed) {
        const styleId = 'fillStyleId' in node ? readStyleId(node.fillStyleId) : null;
        const fills = node.fills;
        for (let i = 0; i < fills.length; i++) {
            const p = fills[i];
            if (!isSolidPaint(p) || p.visible === false)
                continue;
            occ.push({
                nodeId: node.id,
                nodeName: node.name,
                category: 'color',
                property: 'Fill',
                paintProp: 'fills',
                paintIndex: i,
                binding: await paintBinding(p, styleId),
                // stash the resolved value on a symbol-free field via closure below
                ...colorValue(p),
            });
        }
    }
    // Strokes
    if ('strokes' in node) {
        const styleId = 'strokeStyleId' in node ? readStyleId(node.strokeStyleId) : null;
        const strokes = node.strokes;
        for (let i = 0; i < strokes.length; i++) {
            const p = strokes[i];
            if (!isSolidPaint(p) || p.visible === false)
                continue;
            occ.push({
                nodeId: node.id,
                nodeName: node.name,
                category: 'color',
                property: 'Stroke',
                paintProp: 'strokes',
                paintIndex: i,
                binding: await paintBinding(p, styleId),
                ...colorValue(p),
            });
        }
    }
}
// Carries the resolved color forward without leaking figma.mixed into the group step.
function colorValue(paint) {
    const hex8 = colorKey(paint.color, paint.opacity == null ? 1 : paint.opacity);
    return { _key: 'color|' + hex8, _display: colorDisplay(hex8), _swatch: hex8 };
}
async function extractRadius(node, occ) {
    if (!('cornerRadius' in node))
        return;
    const cr = node.cornerRadius;
    const CORNERS = ['topLeftRadius', 'topRightRadius', 'bottomLeftRadius', 'bottomRightRadius'];
    if (cr !== figma.mixed && typeof cr === 'number') {
        if (cr <= 0)
            return;
        const alias = node.boundVariables && node.boundVariables.topLeftRadius;
        occ.push({
            nodeId: node.id,
            nodeName: node.name,
            category: 'radius',
            property: 'Corner radius',
            fields: CORNERS.slice(),
            binding: alias ? await variableBinding(alias) : { type: 'none' },
            _key: 'radius|' + numKey(cr),
            _display: numKey(cr) + 'px',
            _num: numKey(cr),
        });
        return;
    }
    // Mixed corners: one occurrence per corner that has a radius.
    if ('topLeftRadius' in node) {
        for (const field of CORNERS) {
            const value = node[field];
            if (typeof value !== 'number' || value <= 0)
                continue;
            const alias = node.boundVariables && node.boundVariables[field];
            occ.push({
                nodeId: node.id,
                nodeName: node.name,
                category: 'radius',
                property: cornerLabel(field),
                fields: [field],
                binding: alias ? await variableBinding(alias) : { type: 'none' },
                _key: 'radius|' + numKey(value),
                _display: numKey(value) + 'px',
                _num: numKey(value),
            });
        }
    }
}
function cornerLabel(field) {
    switch (field) {
        case 'topLeftRadius':
            return 'Radius ◤';
        case 'topRightRadius':
            return 'Radius ◥';
        case 'bottomLeftRadius':
            return 'Radius ◣';
        case 'bottomRightRadius':
            return 'Radius ◢';
        default:
            return 'Corner radius';
    }
}
const SPACING_FIELDS = [
    { field: 'itemSpacing', label: 'Gap' },
    { field: 'counterAxisSpacing', label: 'Gap (wrap)' },
    { field: 'paddingLeft', label: 'Padding L' },
    { field: 'paddingRight', label: 'Padding R' },
    { field: 'paddingTop', label: 'Padding T' },
    { field: 'paddingBottom', label: 'Padding B' },
];
async function extractSpacing(node, occ) {
    if (!('layoutMode' in node) || node.layoutMode === 'NONE')
        return;
    const bag = node;
    for (const { field, label } of SPACING_FIELDS) {
        const value = bag[field];
        if (typeof value !== 'number' || value <= 0)
            continue;
        const alias = node.boundVariables && node.boundVariables[field];
        occ.push({
            nodeId: node.id,
            nodeName: node.name,
            category: 'spacing',
            property: label,
            fields: [field],
            binding: alias ? await variableBinding(alias) : { type: 'none' },
            _key: 'spacing|' + numKey(value),
            _display: numKey(value) + 'px',
            _num: numKey(value),
        });
    }
}
async function extractTextSize(node, occ) {
    if (node.type !== 'TEXT')
        return;
    const fs = node.fontSize;
    if (fs !== figma.mixed && typeof fs === 'number') {
        const styleId = readStyleId(node.textStyleId);
        const fontVarArr = node.boundVariables && node.boundVariables.fontSize;
        const fontVar = fontVarArr && fontVarArr.length ? fontVarArr[0] : undefined;
        let binding = { type: 'none' };
        if (styleId)
            binding = await styleBinding(styleId);
        else if (fontVar)
            binding = await variableBinding(fontVar);
        occ.push({
            nodeId: node.id,
            nodeName: node.name,
            category: 'textSize',
            property: 'Font size',
            fields: ['fontSize'],
            binding,
            _key: 'textSize|' + numKey(fs),
            _display: numKey(fs) + 'px',
            _num: numKey(fs),
        });
        return;
    }
    // Mixed sizes: emit one occurrence per distinct size range.
    const segments = node.getStyledTextSegments(['fontSize', 'textStyleId']);
    for (const seg of segments) {
        const size = seg.fontSize;
        if (typeof size !== 'number' || size <= 0)
            continue;
        const styleId = seg.textStyleId ? seg.textStyleId : null;
        occ.push({
            nodeId: node.id,
            nodeName: node.name,
            category: 'textSize',
            property: 'Font size (range)',
            fields: ['fontSize'],
            range: { start: seg.start, end: seg.end },
            binding: styleId ? await styleBinding(styleId) : { type: 'none' },
            _key: 'textSize|' + numKey(size),
            _display: numKey(size) + 'px',
            _num: numKey(size),
        });
    }
}
// ----------------------------------------------------------------------------------
// Scan orchestration
// ----------------------------------------------------------------------------------
// Serialise scans and coalesce bursts (e.g. marquee selection fires many events):
// while a scan runs, extra triggers set a flag and one trailing scan runs at the end.
let scanning = false;
let scanQueued = false;
async function runScan() {
    if (scanning) {
        scanQueued = true;
        return;
    }
    scanning = true;
    try {
        do {
            scanQueued = false;
            await scanOnce();
        } while (scanQueued);
    }
    finally {
        scanning = false;
    }
}
async function scanOnce() {
    varCache.clear();
    styleCache.clear();
    const ctx = contextFromScope();
    const nodes = await collectScopeNodes();
    const total = nodes.length;
    const raw = [];
    for (let i = 0; i < total; i++) {
        const node = nodes[i];
        try {
            await extractColors(node, raw);
            await extractRadius(node, raw);
            await extractSpacing(node, raw);
            await extractTextSize(node, raw);
        }
        catch (_e) {
            // Skip nodes we cannot read; keep scanning.
        }
        if (i % 150 === 0 || i === total - 1) {
            figma.ui.postMessage({ type: 'scan-progress', done: i + 1, total });
        }
    }
    const { groups, stats } = buildGroups(raw);
    figma.ui.postMessage({ type: 'scan-result', scope: ctx.scope, contextName: ctx.contextName, groups, stats, nodeCount: total });
}
function buildGroups(raw) {
    const map = new Map();
    for (const r of raw) {
        const key = r._key;
        let group = map.get(key);
        if (!group) {
            group = {
                key,
                category: r.category,
                displayValue: r._display,
                swatch: r._swatch,
                numberValue: r._num,
                occurrences: [],
                count: 0,
                tokenizedCount: 0,
                status: 'raw',
            };
            map.set(key, group);
        }
        // Strip the internal underscore fields before sending to the UI.
        const occ = {
            nodeId: r.nodeId,
            nodeName: r.nodeName,
            category: r.category,
            property: r.property,
            paintProp: r.paintProp,
            paintIndex: r.paintIndex,
            fields: r.fields,
            range: r.range,
            binding: r.binding,
        };
        group.occurrences.push(occ);
    }
    const groups = [];
    const cat = () => ({ tokenized: 0, total: 0, pct: 0 });
    const stats = {
        overall: cat(),
        byCategory: { color: cat(), radius: cat(), spacing: cat(), textSize: cat() },
    };
    for (const group of map.values()) {
        group.count = group.occurrences.length;
        let tokenized = 0;
        const tokenIds = new Set();
        for (const o of group.occurrences) {
            if (o.binding.type !== 'none') {
                tokenized++;
                if (o.binding.tokenId)
                    tokenIds.add(o.binding.tokenId);
            }
        }
        group.tokenizedCount = tokenized;
        if (tokenized === 0) {
            group.status = 'raw'; // nothing linked
        }
        else if (tokenized < group.count) {
            group.status = 'partial'; // at least one occurrence is still unlinked
        }
        else {
            group.status = 'tokenized'; // every occurrence is linked (even if to different tokens)
            if (tokenIds.size === 1) {
                const first = group.occurrences.find((o) => o.binding.tokenName);
                group.tokenName = first ? first.binding.tokenName : undefined;
            }
        }
        const cs = stats.byCategory[group.category];
        cs.total += group.count;
        cs.tokenized += tokenized;
        stats.overall.total += group.count;
        stats.overall.tokenized += tokenized;
        groups.push(group);
    }
    const pct = (s) => (s.pct = s.total === 0 ? 0 : Math.round((s.tokenized / s.total) * 100));
    pct(stats.overall);
    Object.keys(stats.byCategory).forEach((k) => pct(stats.byCategory[k]));
    const rank = { raw: 0, partial: 1, tokenized: 2 };
    groups.sort((a, b) => rank[a.status] - rank[b.status] || b.count - a.count);
    return { groups, stats };
}
// ----------------------------------------------------------------------------------
// Canvas selection
// ----------------------------------------------------------------------------------
async function selectNodes(nodeIds) {
    const nodes = [];
    for (const id of nodeIds) {
        try {
            const node = await figma.getNodeByIdAsync(id);
            if (node && node.type !== 'PAGE' && node.type !== 'DOCUMENT')
                nodes.push(node);
        }
        catch (_e) {
            // node may have been deleted since the scan
        }
    }
    if (nodes.length === 0) {
        figma.ui.postMessage({ type: 'error', message: 'Element not found (it may have been deleted). Please scan again.' });
        return;
    }
    // Mark this as our own selection so the next Scan/Re-scan keeps the current scope
    // instead of narrowing it to just these matched nodes.
    programmaticSelectionKey = selectionKey(nodes);
    figma.currentPage.selection = nodes;
    figma.viewport.scrollAndZoomIntoView(nodes);
}
// ----------------------------------------------------------------------------------
// Apply / merge
// ----------------------------------------------------------------------------------
async function applyToken(occurrences, target) {
    let variable = null;
    if (target.kind === 'variable') {
        variable = target.id ? await figma.variables.getVariableByIdAsync(target.id) : null;
        if (!variable) {
            figma.ui.postMessage({ type: 'error', message: 'Could not load the selected variable.' });
            return;
        }
    }
    let applied = 0;
    const failed = [];
    for (const occ of occurrences) {
        try {
            const node = await figma.getNodeByIdAsync(occ.nodeId);
            if (!node) {
                failed.push({ nodeId: occ.nodeId, reason: 'node not found' });
                continue;
            }
            await applyToNode(node, occ, target, variable);
            applied++;
        }
        catch (e) {
            failed.push({ nodeId: occ.nodeId, reason: e instanceof Error ? e.message : String(e) });
        }
    }
    figma.ui.postMessage({ type: 'apply-done', applied, failed });
    await runScan(); // refresh coverage (scope follows the current selection)
}
async function applyToNode(node, occ, target, variable) {
    if (occ.category === 'color') {
        await applyColor(node, occ, target, variable);
    }
    else if (occ.category === 'radius' || occ.category === 'spacing') {
        const setter = node;
        if (target.kind === 'none') {
            for (const field of occ.fields || [])
                setter.setBoundVariable(field, null); // unlink
        }
        else {
            if (!variable)
                throw new Error('numbers can only be applied via a variable');
            for (const field of occ.fields || [])
                setter.setBoundVariable(field, variable);
        }
    }
    else if (occ.category === 'textSize') {
        await applyTextSize(node, occ, target, variable);
    }
}
async function applyColor(node, occ, target, variable) {
    const prop = occ.paintProp || 'fills';
    const idx = occ.paintIndex == null ? 0 : occ.paintIndex;
    const holder = node;
    if (target.kind === 'none') {
        // Unlink: detach any fill/stroke style and remove any paint-level variable binding
        // (the resolved color stays, the occurrence just becomes raw / No Link).
        if (prop === 'fills' && 'setFillStyleIdAsync' in node)
            await node.setFillStyleIdAsync('');
        else if (prop === 'strokes' && 'setStrokeStyleIdAsync' in node)
            await node.setStrokeStyleIdAsync('');
        const current = prop === 'fills' ? holder.fills : holder.strokes;
        if (current && current !== figma.mixed) {
            const paints = current;
            const paint = paints[idx];
            if (paint && paint.type === 'SOLID' && paint.boundVariables && paint.boundVariables.color) {
                const copy = paints.slice();
                copy[idx] = figma.variables.setBoundVariableForPaint(paint, 'color', null);
                if (prop === 'fills')
                    node.fills = copy;
                else
                    node.strokes = copy;
            }
        }
        return;
    }
    if (target.kind === 'style') {
        const id = target.id || '';
        if (prop === 'fills' && 'setFillStyleIdAsync' in node) {
            await node.setFillStyleIdAsync(id);
        }
        else if (prop === 'strokes' && 'setStrokeStyleIdAsync' in node) {
            await node.setStrokeStyleIdAsync(id);
        }
        else {
            throw new Error('node does not accept a color style');
        }
        return;
    }
    if (!variable)
        throw new Error('missing variable');
    const current = prop === 'fills' ? holder.fills : holder.strokes;
    if (!current || current === figma.mixed)
        throw new Error('paints are mixed/unreadable');
    const copy = current.slice();
    const paint = copy[idx];
    if (!paint || paint.type !== 'SOLID')
        throw new Error('paint is not solid');
    copy[idx] = figma.variables.setBoundVariableForPaint(paint, 'color', variable);
    if (prop === 'fills')
        node.fills = copy;
    else
        node.strokes = copy;
}
async function applyTextSize(node, occ, target, variable) {
    if (node.type !== 'TEXT')
        throw new Error('not a text node');
    if (target.kind === 'none') {
        // Unlink: detach text style and remove any fontSize variable binding.
        if (occ.range) {
            await node.setRangeTextStyleIdAsync(occ.range.start, occ.range.end, '');
        }
        else {
            if ('setTextStyleIdAsync' in node)
                await node.setTextStyleIdAsync('');
            node.setBoundVariable('fontSize', null);
        }
        return;
    }
    if (target.kind === 'style') {
        const id = target.id || '';
        const style = await figma.getStyleByIdAsync(id);
        if (style && style.type === 'TEXT') {
            await figma.loadFontAsync(style.fontName);
        }
        if (occ.range) {
            await node.setRangeTextStyleIdAsync(occ.range.start, occ.range.end, id);
        }
        else {
            await node.setTextStyleIdAsync(id);
        }
        return;
    }
    if (!variable)
        throw new Error('missing variable');
    if (occ.range) {
        node.setRangeBoundVariable(occ.range.start, occ.range.end, 'fontSize', variable);
    }
    else {
        node.setBoundVariable('fontSize', variable);
    }
}
