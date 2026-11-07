
function openEmployeeCard(button) {

    const id = button.dataset.id;
    const name = button.dataset.name;
    const email = button.dataset.email;
    const position = button.dataset.position;
    const department = button.dataset.department;
    const date = button.dataset.date;
    const qr = button.dataset.qr;

    document.getElementById("cardId").textContent = id;
    document.getElementById("cardName").textContent = name;
    document.getElementById("cardEmail").textContent = email;
    document.getElementById("cardPosition").textContent = position;
    document.getElementById("cardDepartment").textContent = department;
    document.getElementById("cardDate").textContent = date;

    document.getElementById("cardAvatar").textContent =
        name.charAt(0).toUpperCase();

    document.getElementById("employeeQRCode").src = qr;

    document.querySelector(".flip-card").classList.remove("flipped");

    openModal("employeeCardModal");
}

function flipEmployeeCard() {
    const card = document.querySelector(".flip-card");
    card.classList.toggle("flipped");

}


function openModal(modalId) {

    document.getElementById(modalId).style.display = "flex";

}


function closeModal(modalId) {

    document.getElementById(modalId).style.display = "none";

}


window.onclick = function(event) {

    if (event.target.classList.contains("modal")) {
        event.target.style.display = "none";
    }

};


document.addEventListener("keydown", function(event) {

    if (event.key === "Escape") {

        document.querySelectorAll(".modal").forEach(function(modal) {
            modal.style.display = "none";
        });

    }

});
