
let isApartment = true;
let apartmentListing = true;
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

function toggleListing(apartment) {
    apartmentListing = apartment;
    updateListingContent();
}

function updateListingContent(){
    const apartmentListingContent = document.getElementById('apartmentListingBtn');
    const subleaseListingContent = document.getElementById('subleaseListingBtn');

    if (apartmentListing) {
        apartmentListingContent.classList.remove('hidden');
        subleaseListingContent.classList.add('hidden');
    } else {
        subleaseListingContent.classList.remove('hidden');
        apartmentListingContent.classList.add('hidden');
    }
}