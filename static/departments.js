const openBtn = document.querySelector(".btn-add");
const modal = document.getElementById("addDeptModal");
const closeBtn = document.getElementById("closeModal");
const cancelBtn = document.getElementById("cancelModal");

openBtn.addEventListener("click", () => {
    modal.style.display = "flex";
});

closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

cancelBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

window.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.style.display = "none";
    }
});
