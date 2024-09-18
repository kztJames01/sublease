
let isMonthly = true;

function togglePricing(monthly) {
    isMonthly = monthly;
    updateButtonStyles();
}

function updateButtonStyles() {
    const monthlyBtn = document.getElementById('monthlyBtn');
    const yearlyBtn = document.getElementById('yearlyBtn');

    if (isMonthly) {
        monthlyBtn.classList.add('custom-btn-filled');
        monthlyBtn.classList.remove('custom-btn-outline');
        yearlyBtn.classList.add('custom-btn-outline');
        yearlyBtn.classList.remove('custom-btn-filled');
    } else {
        yearlyBtn.classList.add('custom-btn-filled');
        yearlyBtn.classList.remove('custom-btn-outline');
        monthlyBtn.classList.add('custom-btn-outline');
        monthlyBtn.classList.remove('custom-btn-filled');
    }
}

// Initial state
updateButtonStyles();
