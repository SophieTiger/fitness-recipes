$(document).ready(function() {
    $('.like-button').click(function(e) {
        e.preventDefault();
        var form = $(this).closest('form');
        $.post(form.attr('action'), form.serialize(), function(data) {
            if (data.liked) {
                $('.like-button i').removeClass('far').addClass('fas').css('color', 'red');
            } else {
                $('.like-button i').removeClass('fas').addClass('far').css('color', '');
            }
            $('#likes-count').text(data.likes_count);
        });
    });
});