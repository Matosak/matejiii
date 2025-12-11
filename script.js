
// Prevent flash of unstyled content (dark mode)
if (localStorage.getItem('darkMode') === 'true' || 
    (localStorage.getItem('darkMode') === null && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
}

document.addEventListener('DOMContentLoaded', function() {
    // Ethical warning v konzoli
    console.log('%c⚠️ REMINDER: Use this tool ethically and legally! ⚠️', 
        'color: white; background-color: #e53e3e; font-size: 14px; padding: 8px; border-radius: 4px;');
});
