const routes = {
    // Top Level
    '#/': 'pages/components.html',
    '#/documentation': 'pages/documentation.html',
    
    // Foundation
    '#/colors': 'pages/foundation/colors.html',
    '#/spacing': 'pages/foundation/spacing.html',
    '#/typography': 'pages/foundation/typography.html',

    // Components
    '#/alert': 'pages/components/alert.html',
    '#/avatar': 'pages/components/avatar.html',
    '#/badge': 'pages/components/badge.html',
    '#/bottomsheet': 'pages/components/bottomsheet.html',
    '#/button': 'pages/components/button.html',
    '#/cell': 'pages/components/cell.html',
    '#/checkbox-radio': 'pages/components/checkbox-radio.html',
    '#/chip': 'pages/components/chip.html',
    '#/input': 'pages/components/input.html',
    '#/modal': 'pages/components/modal.html',
    '#/tab': 'pages/components/tab.html',
    '#/toggle': 'pages/components/toggle.html',
};

const appContent = document.getElementById('app-content');
const navItems = document.querySelectorAll('.nav-item');

async function loadPage() {
    let hash = window.location.hash;

    // Default to components page if no hash
    if (!hash) {
        window.location.hash = '#/';
        return;
    }

    // If route doesn't exist
    if (!routes[hash]) {
        appContent.innerHTML = `
            <div class="content" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; color: var(--text-secondary); text-align: center;">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 16px; color: var(--color-brand-500);"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                <h2 style="margin: 0 0 8px 0; color: var(--text-primary); font-weight: 500;">Page Not Found</h2>
                <p style="margin: 0; font-size: 14px;">The page you are looking for does not exist or hasn't been created yet.</p>
            </div>`;
        updateActiveLink(hash);
        return;
    }

    try {
        // Bust cache in development
        const response = await fetch(`${routes[hash]}?t=${Date.now()}`);
        if (!response.ok) throw new Error('Page not found');

        const html = await response.text();
        appContent.innerHTML = html;

        // Setup copy buttons for newly loaded content
        setupCopyButtons();

        // Build Table of Contents for component/foundation pages
        buildTableOfContents();

        // Setup color swatch copy functionality
        setupColorCopy();

    } catch (error) {
        appContent.innerHTML = `
            <div class="content">
                <h1>404 - Not Found</h1>
                <p class="description">The page you are looking for has not been created yet.</p>
            </div>
        `;
    }

    updateActiveLink(hash);
}

function updateActiveLink(hash) {
    const layout = document.querySelector('.layout');
    
    // Toggle sidebar visibility
    if (hash === '#/' || hash === '#/documentation' || !hash) {
        layout.classList.add('no-sidebar');
        layout.classList.remove('has-toc');
    } else {
        layout.classList.remove('no-sidebar');
        layout.classList.add('has-toc');
    }

    // Sidebar nav items
    navItems.forEach(item => {
        if (item.getAttribute('href') === hash) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });

    // Top nav items
    const topNavLinks = document.querySelectorAll('.top-nav .nav-link');
    topNavLinks.forEach(link => {
        if (hash === '#/documentation' && link.getAttribute('href') === '#/documentation') {
            link.classList.add('active');
        } else if (hash !== '#/documentation' && link.getAttribute('href') === '#/') {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

function setupCopyButtons() {
    const copyButtons = document.querySelectorAll('.usage-copy');
    copyButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const codeBlock = btn.parentElement.nextElementSibling.querySelector('code');
            if (codeBlock) {
                navigator.clipboard.writeText(codeBlock.innerText).then(() => {
                    const originalText = btn.innerHTML;
                    btn.innerHTML = `<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied!`;
                    btn.style.color = "var(--color-green-500, #10b981)";
                    setTimeout(() => {
                        btn.innerHTML = originalText;
                        btn.style.color = "";
                    }, 2000);
                });
            }
        });
    });
}

/**
 * Setup Click-to-Copy for color cards in the Foundation/Colors page
 */
function setupColorCopy() {
    const colorCards = appContent.querySelectorAll('.color-swatch-card');
    if (colorCards.length === 0) return;

    colorCards.forEach(card => {
        const hexElement = card.querySelector('.color-swatch-hex');
        if (!hexElement) return;

        const hexValue = hexElement.innerText.trim();
        card.title = `Click to copy ${hexValue}`;

        card.addEventListener('click', () => {
            navigator.clipboard.writeText(hexValue).then(() => {
                const originalText = hexElement.innerText;
                if (originalText === 'COPIED') return;

                // Feedback
                hexElement.innerText = 'COPIED';
                const originalWeight = hexElement.style.fontWeight;
                const originalColor = hexElement.style.color;
                
                hexElement.style.fontWeight = '700';
                hexElement.style.color = '#10b981'; // Success Green
                
                // Temporary visual scale down
                card.style.transform = 'scale(0.96)';

                setTimeout(() => {
                    hexElement.innerText = originalText;
                    hexElement.style.fontWeight = originalWeight;
                    hexElement.style.color = originalColor;
                    card.style.transform = '';
                }, 1000);
            });
        });
    });
}

// Listen for hash changes
window.addEventListener('hashchange', loadPage);

// Handle sidebar search
function setupSidebarSearch() {
    const searchInput = document.getElementById('component-search');
    const navGroups = document.querySelectorAll('.nav-group');
    
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();

        navGroups.forEach(group => {
            let hasVisibleItems = false;
            const items = group.querySelectorAll('.nav-item');
            
            items.forEach(item => {
                const text = item.textContent.toLowerCase();
                if (text.includes(query)) {
                    item.style.display = 'block';
                    hasVisibleItems = true;
                } else {
                    item.style.display = 'none';
                }
            });

            // Hide the entire group if no items match
            if (hasVisibleItems) {
                group.style.display = 'flex';
            } else {
                group.style.display = 'none';
            }
        });
    });

    // Handle Enter key to navigate to the first visible result
    searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const firstVisibleItem = document.querySelector('.nav-item[style="display: block;"], .nav-item:not([style*="display: none"])');
            if (firstVisibleItem) {
                window.location.hash = firstVisibleItem.getAttribute('href');
                searchInput.blur();
            }
        }
    });
}

// --- Table of Contents (Notion Style) ---
let tocObserver = null;

function buildTableOfContents() {
    const tocNav = document.getElementById('toc-nav');
    if (!tocNav) return;

    // Clean up previous observer
    if (tocObserver) {
        tocObserver.disconnect();
        tocObserver = null;
    }

    // Find all section headings in loaded content
    const headings = appContent.querySelectorAll('h2.section-heading');
    
    // Clear existing ToC
    tocNav.innerHTML = '';

    // Clear existing rail dashes
    const rail = document.getElementById('toc-rail');
    if (rail) rail.innerHTML = '';

    if (headings.length === 0) {
        // No headings found — hide ToC
        document.querySelector('.layout').classList.remove('has-toc');
        return;
    }

    // Build ToC links + rail dashes
    headings.forEach((heading, index) => {
        // Ensure heading has an ID for anchor linking
        if (!heading.id) {
            heading.id = 'section-' + heading.textContent
                .trim()
                .toLowerCase()
                .replace(/[^a-z0-9]+/g, '-')
                .replace(/(^-|-$)/g, '');
        }

        // Create rail dash (one per heading)
        if (rail) {
            const dash = document.createElement('div');
            dash.className = 'toc-rail-dash';
            rail.appendChild(dash);
        }

        const link = document.createElement('a');
        link.className = 'toc-link';
        link.textContent = heading.textContent.trim();
        link.href = 'javascript:void(0)';
        link.dataset.targetId = heading.id;

        // Click-to-scroll + close panel (Notion behavior)
        link.addEventListener('click', (e) => {
            e.preventDefault();
            heading.scrollIntoView({ behavior: 'smooth', block: 'start' });
            // Close panel after clicking (Notion closes on click)
            const container = document.getElementById('toc-container');
            if (container) container.classList.remove('is-open');
        });

        tocNav.appendChild(link);
    });

    // Setup scrollspy via IntersectionObserver
    setupScrollspy(headings);
}

function setupScrollspy(headings) {
    const tocLinks = document.querySelectorAll('.toc-link');
    if (tocLinks.length === 0) return;

    // Use IntersectionObserver to detect which heading is in view
    tocObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove active from all links + dashes
                tocLinks.forEach(link => link.classList.remove('active'));
                const dashes = document.querySelectorAll('.toc-rail-dash');
                dashes.forEach(d => d.classList.remove('active'));

                // Find and activate the matching ToC link
                const activeLink = document.querySelector(
                    `.toc-link[data-target-id="${entry.target.id}"]`
                );
                if (activeLink) {
                    activeLink.classList.add('active');
                    // Sync rail dash by index
                    const linkIndex = Array.from(tocLinks).indexOf(activeLink);
                    if (linkIndex >= 0 && dashes[linkIndex]) {
                        dashes[linkIndex].classList.add('active');
                    }
                }
            }
        });
    }, {
        root: null,
        rootMargin: '0px 0px -70% 0px',
        threshold: 0
    });

    headings.forEach(heading => tocObserver.observe(heading));
}

// --- Rail Click Toggle (Notion behavior) ---
function setupTocRail() {
    const rail = document.getElementById('toc-rail');
    const container = document.getElementById('toc-container');
    if (!rail || !container) return;

    rail.addEventListener('click', (e) => {
        e.stopPropagation();
        container.classList.toggle('is-open');
    });

    // Click outside to close
    document.addEventListener('click', (e) => {
        if (!container.contains(e.target)) {
            container.classList.remove('is-open');
        }
    });
}

// Load initial page
window.addEventListener('DOMContentLoaded', () => {
    loadPage();
    setupSidebarSearch();
    setupTocRail();
});
