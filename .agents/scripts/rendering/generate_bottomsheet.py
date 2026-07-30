import re

content = """<div class="content">

    <!-- Section 1: Page Header -->
    <div class="page-header" style="margin-bottom: 32px;">
        <h1 style="margin-bottom: 8px;">Bottom Sheet</h1>
        <p class="description" style="font-size: 1.125rem; color: var(--color-gray-600); max-width: 750px;">
            Bottom sheet là panel trượt lên từ đáy màn hình, dùng để hiển thị nội dung bổ sung, biểu mẫu, hoặc hành động mà không rời khỏi bối cảnh (context) hiện tại.
        </p>
    </div>

    <!-- Section 2: The Hero Demo -->
    <div class="hero-demo" style="margin-top: 32px;">
        <div style="padding: 64px; display: flex; justify-content: center; align-items: center; background: #f8fafc; border-bottom: 1px solid rgba(226, 232, 240, 0.8);">
            
            <!-- Type: 1 Button -->
            <div style="width: 375px; background: #ffffff; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.08); overflow: hidden;">
                <!-- Top Navigation Bar (padding: 20px 20px 0px) -->
                <div style="padding: 20px 20px 0px 20px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1E293B">
                        <path d="M18 6L6 18M6 6l12 12" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                </div>
                
                <!-- Body (padding: 16px) -->
                <div style="padding: 16px; display: flex; flex-direction: column; gap: 24px;">
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="font-family: 'SF Pro Display', sans-serif; font-size: 24px; font-weight: 700; color: #1E293B;">Title</div>
                        <div style="font-family: 'SF Pro Display', sans-serif; font-size: 14px; font-weight: 400; color: #64748B;">Description text</div>
                    </div>
                    
                    <div style="width: 100%; background: #3B82F6; color: white; height: 48px; border-radius: 24px; display: flex; align-items: center; justify-content: center; font-family: 'SF Pro Display', sans-serif; font-weight: 600; font-size: 16px;">
                        Primary Action
                    </div>
                </div>
                <!-- Home Indicator (mocked) -->
                <div style="height: 34px; padding-bottom: 8px; display: flex; align-items: flex-end; justify-content: center;">
                    <div style="width: 134px; height: 5px; background: #000; border-radius: 100px;"></div>
                </div>
            </div>

        </div>
        <div class="usage-pane" style="margin: 32px;">
            <div class="usage-header"><span class="usage-lang">React</span><button class="usage-copy">Copy</button></div>
            <div class="usage-content">
<pre><code>import { BottomSheet, Button } from "@gds/components";

function App() {
  return (
    &lt;BottomSheet 
      open={true} 
      type="1 button"
      title="Title"
      description="Description text"
    &gt;
      &lt;Button variant="primary" block&gt;Primary Action&lt;/Button&gt;
    &lt;/BottomSheet&gt;
  )
}</code></pre>
            </div>
        </div>
    </div>

    <!-- Section 3: Installation & Usage -->
    <h2 class="section-heading" id="installation-usage" style="margin-top: 48px;">Installation &amp; Usage</h2>
    <h3 style="margin-top: 24px; font-size: 1.125rem;">Installation</h3>
    <div class="usage-pane">
        <div class="usage-header">
            <span class="usage-lang">HTML / CSS</span>
            <button class="usage-copy">Copy</button>
        </div>
        <div class="usage-content">
            <pre><code>&lt;link rel="stylesheet" href="styles/components/bottomsheet.css"&gt;</code></pre>
        </div>
    </div>

    <h3 style="margin-top: 24px; font-size: 1.125rem;">Usage</h3>
    <p style="margin-bottom: 16px; color: var(--color-gray-600);">Sheet bắt buộc bao gồm Top Navigation Bar (icon đóng và tiêu đề) và Body section cấu trúc auto-layout column.</p>

    <!-- Section 4: Examples / Variants -->
    <h2 class="section-heading" id="examples" style="margin-top: 48px;">Variants</h2>

    <!-- No Title -->
    <h3 class="subsection-heading" id="variant-notitle" style="margin-top: 24px; font-size: 1.25rem;">No title</h3>
    <p style="margin-bottom: 16px; color: var(--color-gray-600);">Sheet cơ bản chỉ có navigation bar + body trống.</p>
    <div class="variant-showcase" style="padding: 32px 0;">
        <div style="background: #f8fafc; padding: 48px; border-radius: 12px; display: flex; justify-content: center; align-items: center; border: 1px solid #e2e8f0;">
            <div style="width: 375px; background: #ffffff; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.08); overflow: hidden;">
                <!-- Top Navigation Bar -->
                <div style="padding: 20px 20px 0px 20px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1E293B">
                        <path d="M18 6L6 18M6 6l12 12" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                </div>
                <!-- Empty Body padding -->
                <div style="padding: 16px; min-height: 80px;"></div>
                <!-- Home Indicator -->
                <div style="height: 34px; padding-bottom: 8px; display: flex; align-items: flex-end; justify-content: center;">
                    <div style="width: 134px; height: 5px; background: #000; border-radius: 100px;"></div>
                </div>
            </div>
        </div>
    </div>

    <!-- Search bar -->
    <h3 class="subsection-heading" id="variant-search" style="margin-top: 48px; font-size: 1.25rem;">Search bar</h3>
    <p style="margin-bottom: 16px; color: var(--color-gray-600);">Có ô tìm kiếm trong body (border-radius 999px).</p>
    <div class="variant-showcase" style="padding: 32px 0;">
        <div style="background: #f8fafc; padding: 48px; border-radius: 12px; display: flex; justify-content: center; align-items: center; border: 1px solid #e2e8f0;">
            <div style="width: 375px; background: #ffffff; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.08); overflow: hidden;">
                <!-- Top Navigation Bar -->
                <div style="padding: 20px 20px 0px 20px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1E293B">
                        <path d="M18 6L6 18M6 6l12 12" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                </div>
                <!-- Body with Search -->
                <div style="padding: 16px;">
                    <div style="background: #F1F5F9; border-radius: 999px; height: 36px; padding: 0 16px; display: flex; align-items: center; color: #94A3B8; font-family: 'SF Pro Display', sans-serif; font-size: 14px;">
                        Search...
                    </div>
                </div>
                <!-- Home Indicator -->
                <div style="height: 34px; padding-bottom: 8px; display: flex; align-items: flex-end; justify-content: center;">
                    <div style="width: 134px; height: 5px; background: #000; border-radius: 100px;"></div>
                </div>
            </div>
        </div>
    </div>

</div>
"""

with open('/Users/tuanvq/Documents/gds-myvnpt-wiki/design-docs/pages/components/bottomsheet.html', 'w', encoding='utf-8') as f:
    f.write(content)

