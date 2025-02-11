const menuToggle = document.querySelectorAll('.menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');

menuToggle.forEach((button) => {
    button.addEventListener('click', () => {
        toggleButton();
    });
});

function toggleButton() {
    mobileMenu.classList.toggle('hidden');
}
