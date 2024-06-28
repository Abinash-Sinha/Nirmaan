function toggleTheme() {
    document.body.classList.toggle('dark-mode');
}

function removeForm(button) {
    $(button).closest('.item-form').remove();
    updateFormIndices();
}

function updateFormIndices() {
    var forms = $('#formset .item-form');
    $('#id_form-TOTAL_FORMS').val(forms.length);
    forms.each(function(index) {
        $(this).find(':input').each(function() {
            var name = $(this).attr('name').replace(/-\d+-/, '-' + index + '-');
            $(this).attr('name', name);
            var id = $(this).attr('id').replace(/-\d+-/, '-' + index + '-');
            $(this).attr('id', id);
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureBtn = document.getElementById('captureBtn');
    const image_data = document.getElementById('image_data');

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            video.srcObject = stream;
            video.play();
        })
        .catch(function(err) {
            console.error("Error accessing the webcam: " + err);
        });

    captureBtn.addEventListener('click', function() {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
        const imageDataUrl = canvas.toDataURL('image/jpeg');
        image_data.value = imageDataUrl;
        alert('Image captured from webcam!');
    });

    document.getElementById('image').addEventListener('change', function(e) {
        var fileName = e.target.files[0].name;
        var nextSibling = e.target.nextElementSibling;
        nextSibling.innerText = fileName;
    });
    $('#add-more').click(function () {
        var form_idx = $('#id_form-TOTAL_FORMS').val();
        var form_html = $('#empty-form').html().replace(/__prefix__/g, form_idx);
        $('#formset').append(form_html);
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });
});
