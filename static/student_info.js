document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("studentInfoForm");
    if (!form) return;

    const submitBtn = document.getElementById("button");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const campus = document.getElementById("campus").value;
        const department = document.getElementById("department").value;
        const semester = document.getElementById("semester").value;
        const section = document.getElementById("section").value;

        // Validate selections
        if (!campus || !department || !semester || !section) {
            alert("Please select all fields");
            return;
        }

        // Disable button to prevent double submission
        submitBtn.disabled = true;
        submitBtn.textContent = "Submitting...";

        fetch("/get_timetable", {   // Call Flask route for timetable
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ campus, department, semester, section })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                alert("Timetable fetched successfully!");
                form.reset();
                window.location.href = "/dashboard"; 
            } else {
                alert(data.message || "Failed to fetch timetable. Try again.");
            }
        })
        .catch(err => {
            console.error(err);
            alert("Server error. Try again later.");
        })
        .finally(() => {
            submitBtn.disabled = false;
            submitBtn.textContent = "Submit";
        });
    });

});
