const menuToggle = document.querySelectorAll('.menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');

menuToggle.forEach((button) => {
    button.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
});


