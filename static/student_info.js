// Wait until the HTML content is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    // Get the student info form by its ID
    const form = document.getElementById("studentInfoForm");
    if (!form) return; // Stop if form is not found

    // Listen for form submission
    form.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent default form submission (page reload)

        // Get values from each dropdown by their IDs
        const campus = document.getElementById("campus").value;
        const department = document.getElementById("department").value;
        const semester = document.getElementById("semester").value;
        const section = document.getElementById("section").value;

        // Simple validation: check if any field is empty
        if (!campus || !department || !semester || !section) {
            alert("Please select all fields"); // Show warning to user
            return; // Stop submission
        }

        // Send the student info to the Flask backend using fetch API
        fetch("/student-info", {
            method: "POST", // POST request
            headers: { "Content-Type": "application/json" }, // Sending JSON data
            body: JSON.stringify({
                campus,
                department,
                semester,
                section
            })
        })
        .then(res => res.json()) // Parse JSON response
        .then(data => {
            alert("Student info saved"); // Notify success
            window.location.href = "/dashboard"; // Redirect to dashboard
        })
        .catch(() => alert("Server error")); // Notify if something goes wrong
    });

});
