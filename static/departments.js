/**
 * Final Updated Department Logic (With Conflict Resolution)
 */

// --- 1. Modal Control ---
function showAddDeptModal() {
    const modal = document.getElementById("addDeptModal");
    if (modal) modal.style.display = "flex";
}

function closeDeptModal() {
    const modal = document.getElementById("addDeptModal");
    if (modal) {
        modal.style.display = "none";
        document.getElementById('addDepartmentForm').reset();
        document.getElementById('modalTitle').innerText = "Add Department";
        // Reset the original code storage
        document.querySelector('input[name="department_code"]').removeAttribute('data-original');
    }
}

// --- 2. Edit & Delete Logic ---
function editDepartment(element) {
    const row = element.closest('tr');
    const deptName = row.querySelector('.name').innerText.trim();
    const deptCode = row.querySelector('.sub').innerText.trim();
    const teachers = row.querySelector('.tag.blue').innerText.replace(/[^0-9]/g, '');
    const subjects = row.querySelector('.tag.purple').innerText.replace(/[^0-9]/g, '');

    const codeInput = document.querySelector('input[name="department_code"]');
    
    document.getElementById('deptName').value = deptName;
    codeInput.value = deptCode;
    // Store original code to skip duplicate check for ITSELF during edit
    codeInput.setAttribute('data-original', deptCode.toUpperCase());
    
    document.querySelector('input[name="total_teachers"]').value = teachers;
    document.querySelector('input[name="total_subjects"]').value = subjects;

    document.getElementById('modalTitle').innerText = "Edit Department";
    showAddDeptModal();
}

function deleteItem(element) {
    if(confirm("Are you sure you want to delete this record?")) {
        element.closest('tr').remove();
    }
}

// --- 3. Validation & Duplicate Prevention ---
document.addEventListener('DOMContentLoaded', function() {
    const deptForm = document.getElementById('addDepartmentForm');

    if (deptForm) {
        deptForm.addEventListener('submit', function(event) {
            const codeField = document.querySelector('input[name="department_code"]');
            const codeInput = codeField.value.trim().toUpperCase();
            const originalCode = codeField.getAttribute('data-original'); // Only exists in Edit mode
            const isEdit = document.getElementById('modalTitle').innerText === "Edit Department";

            // Get all codes currently in the table
            const currentCodes = Array.from(document.querySelectorAll('.sub'))
                                     .map(el => el.innerText.trim().toUpperCase());

            // --- Logic Check ---
            if (isEdit) {
                // Agar user ne code badal diya hai aur naya code pehle se kisi aur row mein hai
                if (codeInput !== originalCode && currentCodes.includes(codeInput)) {
                    event.preventDefault();
                    alert("ERROR: The code '" + codeInput + "' is already used by another department.");
                    return;
                }
            } else {
                // Agar Naya Department add ho raha hai aur code pehle se table mein hai
                if (currentCodes.includes(codeInput)) {
                    event.preventDefault();
                    alert("ERROR: The Department Code '" + codeInput + "' already exists! Please use a unique code.");
                    return;
                }
            }
        });
    }

    // Modal Close buttons setup
    const closeBtn = document.getElementById('closeModal');
    const cancelBtn = document.getElementById('cancelModal');
    if (closeBtn) closeBtn.onclick = closeDeptModal;
    if (cancelBtn) cancelBtn.onclick = closeDeptModal;
});

// Close modal if user clicks outside
window.onclick = function(event) {
    const modal = document.getElementById("addDeptModal");
    if (event.target == modal) closeDeptModal();
}