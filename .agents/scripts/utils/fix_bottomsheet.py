import re

with open('/Users/tuanvq/Documents/gds-myvnpt-wiki/design-docs/pages/components/bottomsheet.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the hero-demo part inside bottomsheet.html
new_hero = """    <!-- Section 2: The Hero Demo -->
    <div class="hero-demo" style="margin-top: 32px;">
        <div style="padding: 64px; display: flex; justify-content: center; align-items: center; background: #f8fafc; border-bottom: 1px solid rgba(226, 232, 240, 0.8);">
            
            <div style="width: 375px; background: #ffffff; border-radius: 16px; padding: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.08);">
                <div style="display: flex; flex-direction: column;">
                    <!-- Close button -->
                    <div style="margin-bottom: 16px;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1E293B">
                            <path d="M18 6L6 18M6 6l12 12" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </div>
                    
                    <!-- Content -->
                    <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px;">
                        <div style="font-family: 'SF Pro Display', sans-serif; font-size: 24px; font-weight: 700; color: #1E293B;">Title</div>
                        <div style="font-family: 'SF Pro Display', sans-serif; font-size: 14px; font-weight: 400; color: #64748B;">Description text</div>
                    </div>
                    
                    <!-- Action -->
                    <div style="width: 100%; background: #3B82F6; color: white; height: 48px; border-radius: 24px; display: flex; align-items: center; justify-content: center; font-family: 'SF Pro Display', sans-serif; font-weight: 600; font-size: 16px;">
                        Primary Action
                    </div>
                </div>
            </div>

        </div>"""

content = re.sub(r'    <!-- Section 2: The Hero Demo -->.*?</div>\s+</div>', new_hero + '\n        <div class="usage-pane" style="margin: 32px;">\n            <div class="usage-header"><span class="usage-lang">React</span><button class="usage-copy">Copy</button></div>\n            <div class="usage-content">\n<pre><code>import { BottomSheet, Button } from "@gds/components";\n\nfunction App() {\n  return (\n    &lt;BottomSheet \n      open={true} \n      type="1 button"\n      title="Title"\n      description="Description text"\n    &gt;\n      &lt;Button variant="primary" block&gt;Primary Action&lt;/Button&gt;\n    &lt;/BottomSheet&gt;\n  )\n}</code></pre>\n            </div>\n        </div>\n    </div>', content, flags=re.DOTALL)

with open('/Users/tuanvq/Documents/gds-myvnpt-wiki/design-docs/pages/components/bottomsheet.html', 'w', encoding='utf-8') as f:
    f.write(content)
