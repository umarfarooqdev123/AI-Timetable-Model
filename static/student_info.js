document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("studentInfoForm");
    if (!form) return;

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const campus = document.getElementById("campus").value;
        const department = document.getElementById("department").value;
        const semester = document.getElementById("semester").value;
        const section = document.getElementById("section").value;

        if (!campus || !department || !semester || !section) {
            alert("Please select all fields");
            return;
        }

        fetch("/student-info", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                campus,
                department,
                semester,
                section
            })
        })
        .then(res => res.json())
        .then(data => {
            alert("Student info saved");
            window.location.href = "/dashboard";
        })
        .catch(() => alert("Server error"));
    });

});
