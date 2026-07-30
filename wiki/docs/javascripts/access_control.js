(function () {
    const EXPECTED_HASH = "Z2RzQHB0c3A=";
    const SESSION_DURATION_MS = 24 * 60 * 60 * 1000; // 24 hours

    function checkAccess() {
        const currentAccess = localStorage.getItem('tm_access_level');
        const loginTime = localStorage.getItem('tm_login_time');

        // Check for 24h expiration on full access
        if (currentAccess === 'full_access' && loginTime) {
            const now = new Date().getTime();
            if (now - parseInt(loginTime, 10) > SESSION_DURATION_MS) {
                // Expired
                localStorage.removeItem('tm_access_level');
                localStorage.removeItem('tm_login_time');
                return null;
            }
        }
        return currentAccess; // 'full_access', 'view_only', or null
    }

    // Export to global scope
    window.TM_CONFIG = window.TM_CONFIG || {};
    window.TM_CONFIG.checkAccess = checkAccess;
    window.TM_CONFIG.EXPECTED_HASH = EXPECTED_HASH;

    // Apply basic restrictions for Mkdocs pages
    window.applySiteWideViewOnlyRestrictions = function () {
        // Nothing inherently restricted for just viewing documentation
        // This is a placeholder if we need to hide specific MkDocs elements
    };

    window.grantSiteAccess = function (mode) {
        document.getElementById('tm-access-modal-overlay').style.display = 'none';
        document.body.classList.remove('access-locked');

        if (mode === 'full_access') {
            localStorage.setItem('tm_access_level', 'full_access');
            localStorage.setItem('tm_login_time', new Date().getTime().toString());
        } else {
            localStorage.setItem('tm_access_level', 'view_only');
            // View only doesn't expire
            localStorage.removeItem('tm_login_time');
        }

        // Update the global indicator in the MkDocs header or Task manager sidebar
        if (window.updateSidebarIndicator) {
            window.updateSidebarIndicator(mode);
        } else {
            window.updateGlobalIndicator(mode);
        }

        if (mode === 'view_only') {
            if (window.applyViewOnlyRestrictions) {
                window.applyViewOnlyRestrictions(); // Applies to task manager
            } else {
                window.applySiteWideViewOnlyRestrictions(); // Applies to mkdocs
            }
        } else {
            // For task manager
            const addTaskBtn = document.getElementById('tm-btn-add-task');
            if (addTaskBtn) addTaskBtn.style.display = 'flex';
        }
    };

    window.updateGlobalIndicator = function (mode) {
        const indicatorText = document.getElementById('global-view-mode-text');
        const indicatorDiv = document.getElementById('global-view-mode-indicator');
        const indicatorIcon = document.getElementById('global-view-mode-icon');

        if (!indicatorText || !indicatorDiv || !indicatorIcon) return;

        if (mode === 'full_access') {
            indicatorText.innerHTML = 'Mode: Full Access';
            indicatorText.style.color = '#a7f3d0';
            indicatorIcon.style.color = '#a7f3d0';
            indicatorIcon.innerHTML = '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>';
        } else {
            indicatorText.innerHTML = 'Mode: View Only';
            indicatorText.style.color = 'white';
            indicatorIcon.style.color = 'white';
            indicatorIcon.innerHTML = '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle>';
        }
    };

    window.openAccessModalManually = function () {
        const overlay = document.getElementById('tm-access-modal-overlay');
        if (overlay) {
            overlay.style.display = 'flex';
            document.getElementById('tm-access-close-btn').style.display = 'block';
            window.hideLoginForm();
        }
    };

    window.closeAccessModal = function () {
        const overlay = document.getElementById('tm-access-modal-overlay');
        if (overlay) overlay.style.display = 'none';
    };

    window.showLoginForm = function () {
        document.getElementById('tm-access-cards').style.display = 'none';
        document.getElementById('tm-login-form').style.display = 'block';
        setTimeout(() => document.getElementById('tm-access-password').focus(), 100);
    };

    window.hideLoginForm = function () {
        document.getElementById('tm-access-cards').style.display = 'flex';
        document.getElementById('tm-login-form').style.display = 'none';
        document.getElementById('tm-login-error').style.display = 'none';
        document.getElementById('tm-access-password').value = '';
    };

    window.selectAccessMode = function (mode) {
        if (mode === 'view_only') {
            window.grantSiteAccess('view_only');
            if (window.hasGrantedAccessOnce) window.location.reload();
        } else if (mode === 'full_access') {
            const pwdInput = document.getElementById('tm-access-password');
            const errorMsg = document.getElementById('tm-login-error');
            const inputVal = pwdInput.value;
            try {
                const hashedInput = btoa(inputVal);
                if (hashedInput === window.TM_CONFIG.EXPECTED_HASH) {
                    window.grantSiteAccess('full_access');
                    if (window.hasGrantedAccessOnce) window.location.reload();
                } else {
                    errorMsg.style.display = 'block';
                }
            } catch (e) {
                errorMsg.style.display = 'block';
            }
        }
    };

    document.addEventListener('DOMContentLoaded', () => {
        const currentAccess = checkAccess();
        if (currentAccess) {
            window.grantSiteAccess(currentAccess);
        } else {
            // Show modal if not set or expired
            const overlay = document.getElementById('tm-access-modal-overlay');
            if (overlay) {
                overlay.style.display = 'flex';
                document.body.classList.add('access-locked');
            }
        }
    });

})();
