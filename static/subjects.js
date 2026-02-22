document.addEventListener('DOMContentLoaded', function() {
    const subForm = document.getElementById('addSubjectForm');

    if (subForm) {
        subForm.addEventListener('submit', function(event) {
            event.preventDefault(); 
            
            const name = document.getElementById("subjectName").value.trim();
            const code = document.getElementById("subjectCode").value.trim();

            if (name === "" || code === "") {
                // Professional English Message
                alert("Validation Error: Please provide both the Subject Name and Subject Code to proceed.");
            } else {
                handleSave(); 
            }
        });
    }
});