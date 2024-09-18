const saveButtons = document.querySelectorAll('.saveButton');
saveButtons.forEach(button => {
    let isSaved = false;
    button.addEventListener('click', function () {
        toggleSave();
    });
    function toggleSave() {
        const icon = button.querySelector('.saveIcon');

        isSaved = !isSaved;
        if (isSaved) {
            button.classList.remove('text-teal-500');
            button.classList.add('text-red-800', 'border-red-800');
            icon.name = 'heart';
            alert('Added to saved list!');
        } else {
            button.classList.remove('text-red-800', 'border-red-800');
            button.classList.add('text-teal-500');
            icon.name = 'heart-outline';
            alert('Removed from saved list!');
        }
    }
});