
    const scroll = document.getElementById('scroll');
        scroll.addEventListener('click', () => {
        document.getElementById('apartmentListingBtn').scrollIntoView({ behavior: 'smooth' });
        })
    $(document).ready(function () {
        $('#apartmentListingBtn').click(function (e) {
            e.preventDefault();
            loadContent('newAL/');
        });

    $('#subleaseListingBtn').click(function (e) {
        e.preventDefault();
    loadContent('newIL/');
            });

    function loadContent(url) {
        $.ajax({
            url: url,
            type: 'GET',
            success: function (data) {
                $('#listingContent').html(data);
            },
            error: function (xhr, status, error) {
                console.error('Error loading content:', error);
            }
        });
            }
        });
    const apartmentListingBtn = document.getElementById('apartmentListingBtn');
    const subleaseListingBtn = document.getElementById('subleaseListingBtn');

    function togglePricing(bool) {
        if (bool) {
        apartmentListingBtn.classList.remove('custom-btn-outline');
    apartmentListingBtn.classList.add('custom-btn-filled');
    subleaseListingBtn.classList.remove('custom-btn-filled');
    subleaseListingBtn.classList.add('custom-btn-outline');
        }
    else {
        apartmentListingBtn.classList.remove('custom-btn-filled');
    apartmentListingBtn.classList.add('custom-btn-outline');
    subleaseListingBtn.classList.remove('custom-btn-outline');
    subleaseListingBtn.classList.add('custom-btn-filled');
        }
       
    }


