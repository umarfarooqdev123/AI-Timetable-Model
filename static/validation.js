// Jab page poora load ho jaye tab ye kaam kare
document.addEventListener('DOMContentLoaded', function() {
    
    // 1. Subject Form ki validation
    const subjectForm = document.querySelector('form[action*="subjects"]'); 
    
    if (subjectForm) {
        subjectForm.addEventListener('submit', function(event) {
            // Input fields ko dhoondna
            const nameInput = subjectForm.querySelector('input[name="subject_name"]');
            const codeInput = subjectForm.querySelector('input[name="subject_code"]');

            // Agar fields khali hain to error dikhana
            if (nameInput.value.trim() === "" || codeInput.value.trim() === "") {
                alert("Opps! Meharbani karke Subject Name aur Code dono likhein.");
                event.preventDefault(); // Ye form ko submit hone se rok dega
            }
        });
    }
});