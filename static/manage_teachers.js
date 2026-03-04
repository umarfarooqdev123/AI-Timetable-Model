// manage_teachers.js

document.addEventListener('DOMContentLoaded', () => {

    // -------------------
    // Add Teacher Modal
    // -------------------
    const addTeacherModal = document.getElementById('addTeacherModal');
    const addTeacherBtn = document.querySelector('.add-teacher-btn');
    const addCancelBtn = addTeacherModal.querySelector('.cancel-btn');

    // Open Add Modal
    if (addTeacherBtn) {
        addTeacherBtn.addEventListener('click', () => {
            addTeacherModal.style.display = 'flex';
        });
    }

    // Close Add Modal
    if (addCancelBtn) {
        addCancelBtn.addEventListener('click', () => {
            addTeacherModal.style.display = 'none';
        });
    }

    // Close Add Modal on clicking outside modal content
    addTeacherModal.addEventListener('click', (e) => {
        if (e.target === addTeacherModal) {
            addTeacherModal.style.display = 'none';
        }
    });

    // -------------------
    // Edit Teacher Modals
    // -------------------
    const editModals = document.querySelectorAll('[id^="editTeacherModal"]');

    editModals.forEach((modal) => {
        const closeBtn = modal.querySelector('.modal-header i');
        const cancelBtn = modal.querySelector('.cancel-btn');

        // Close button (X)
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                modal.style.display = 'none';
            });
        }

        // Cancel button
        if (cancelBtn) {
            cancelBtn.addEventListener('click', () => {
                modal.style.display = 'none';
            });
        }

        // Close modal on clicking outside
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        });
    });

    // -------------------
    // Optional: Escape key to close modals
    // -------------------
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            // Close Add Teacher Modal
            if (addTeacherModal.style.display === 'flex') {
                addTeacherModal.style.display = 'none';
            }

            // Close all Edit Modals
            editModals.forEach((modal) => {
                if (modal.style.display === 'flex') {
                    modal.style.display = 'none';
                }
            });
        }
    });
});