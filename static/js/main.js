// Main JavaScript file for C.U.M

// Add CSRF token to all HTMX requests
document.addEventListener('htmx:configRequest', function(evt) {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    evt.detail.headers['X-CSRFToken'] = csrfToken;
});

// Show loading indicator during HTMX requests
document.addEventListener('htmx:beforeRequest', function(evt) {
    const target = evt.detail.target;
    if (target.tagName === 'BUTTON') {
        target.disabled = true;
        target.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';
    }
});

// Reset button state after HTMX request
document.addEventListener('htmx:afterRequest', function(evt) {
    const target = evt.detail.target;
    if (target.tagName === 'BUTTON') {
        target.disabled = false;
        const originalText = target.getAttribute('data-original-text');
        if (originalText) {
            target.innerHTML = originalText;
        }
    }
});

// Store original button text before HTMX request
document.addEventListener('htmx:beforeRequest', function(evt) {
    const target = evt.detail.target;
    if (target.tagName === 'BUTTON' && !target.getAttribute('data-original-text')) {
        target.setAttribute('data-original-text', target.innerHTML);
    }
}); 