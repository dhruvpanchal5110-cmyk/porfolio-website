const hamburger = document.getElementById("hamburger");
const links = document.querySelector(".links");

hamburger.addEventListener("click", () => {
    links.classList.toggle("active");
});
