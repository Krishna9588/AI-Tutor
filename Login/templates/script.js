function showForm(formType) {
    // Toggle buttons
    document.querySelectorAll('.toggle-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');

    // Toggle forms
    document.querySelectorAll('.form-container').forEach(form => {
        form.classList.remove('active');
    });
    document.getElementById(`${formType}-form`).classList.add('active');
}

function validateRegistration() {
    const password = document.getElementById('reg-password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    const errorElement = document.getElementById('password-error');

    if (password.length < 8) {
        errorElement.textContent = "Password must be at least 8 characters!";
        errorElement.style.display = 'block';
        return false;
    }
    
    if (password !== confirmPassword) {
        errorElement.textContent = "Passwords do not match!";
        errorElement.style.display = 'block';
        return false;
    }
    
    errorElement.style.display = 'none';
    return true;
}