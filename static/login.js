
document.addEventListener('DOMContentLoaded', () => {
    const splash = document.getElementById('splash-screen');
    const loginPage = document.getElementById('login-page');
    const loginContainer = document.querySelector('.login-card');

    
    if (splash) splash.style.display = 'none'; 
    
    if (loginPage) {
        loginPage.style.opacity = '1';
        loginPage.style.visibility = 'visible';
    }
    
    if (loginContainer) {
        loginContainer.style.opacity = '1';
        loginContainer.style.transform = 'translateY(0)';
    }

    // 2. Form Validation
    const loginForm = document.querySelector('form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const passwordField = document.querySelector('input[type="password"]');
            const password = passwordField.value;
            
            if (password.length < 3) {
                e.preventDefault(); // Stop form from sending to Python
                alert("Password is too short! Please enter at least 3 characters.");
                passwordField.style.borderColor = "red";
            }
        });
    }

    // Allow scrolling on the login page
    document.body.style.overflow = 'auto';
});