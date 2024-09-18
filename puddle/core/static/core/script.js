
let isApartment = true;

function togglePricing(apartment) {
    isApartment = apartment;
    updateButtonStyles();
    updateContent();
}

function updateButtonStyles() {
    const apartmentBtn = document.getElementById('apartmentBtn');
    const subleasesBtn = document.getElementById('subleasesBtn');

    if (isApartment) {
        apartmentBtn.classList.add('custom-btn-filled');
        apartmentBtn.classList.remove('custom-btn-outline');
        subleasesBtn.classList.add('custom-btn-outline');
        subleasesBtn.classList.remove('custom-btn-filled');
    } else {
        subleasesBtn.classList.add('custom-btn-filled');
        subleasesBtn.classList.remove('custom-btn-outline');
        apartmentBtn.classList.add('custom-btn-outline');
        apartmentBtn.classList.remove('custom-btn-filled');
    }
}

function updateContent(){
    const apartmentContent = document.getElementById('apartmentContent');
    const subleaseContent = document.getElementById('subleaseContent');

    if(isApartment){
        apartmentContent.classList.remove('hidden');
        subleaseContent.classList.add('hidden');
    }else{
        subleaseContent.classList.remove('hidden'); 
        apartmentContent.classList.add('hidden');
    }
}
updateContent();
updateButtonStyles(); //initial state

