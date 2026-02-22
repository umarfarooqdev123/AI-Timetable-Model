document.addEventListener('DOMContentLoaded', function() {
    
    // 1. Department Form Validation
    const deptForm = document.getElementById('addDepartmentForm');
    if (deptForm) {
        deptForm.addEventListener('submit', function(event) {
            const dName = document.getElementById('deptName').value.trim();
            if (dName === "") {
                alert("Department ka naam likhna zaroori hai!");
                event.preventDefault(); // Form submit hone se rok dega
            }
        });
    }

    // 2. Subject Form Validation
    const subForm = document.getElementById('addSubjectForm');
    if (subForm) {
        subForm.addEventListener('submit', function(event) {
            const sName = document.getElementById('subjectName').value.trim();
            const sCode = document.getElementById('subjectCode').value.trim();
            if (sName === "" || sCode === "") {
                alert("Subject Name aur Code dono fill karein!");
                event.preventDefault();
            }
        });
    }
});