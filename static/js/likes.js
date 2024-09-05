console.log("Likes.js loaded");

$(document).ready(function() {
    // Define variables
    const likeButtons = $('.like-button');
    const messageContainer = $('.col-md-8.offset-md-2');

    likeButtons.click(function(e) {
        e.preventDefault();  // Prevent the default form submission
        var form = $(this).closest('form');
        var button = $(this);  // Store reference to the clicked button
        
        $.ajax({
            url: form.attr('action'),
            type: 'POST',
            data: form.serialize(),
            dataType: 'json',
            success: function(data) {
                if (data.liked) {
                    button.find('i').removeClass('far').addClass('fas').css('color', 'red');
                } else {
                    button.find('i').removeClass('fas').addClass('far').css('color', '');
                }
                button.siblings('.likes-count').text(data.likes_count);
                
                // Display the message
                showMessage(data.message);
            },
            error: function(xhr, status, error) {
                console.error("An error occurred: " + error);
                showMessage("An error occurred while processing your request.");
            }
        });
    });

    function showMessage(message) {
        // Create the message element
        var messageHtml = `
            <div class="alert alert-success alert-dismissible fade show" id="msg" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;

        // Insert the message into the messages container
        messageContainer.html(messageHtml);

        // Fade out the message after 3 seconds
        setTimeout(function() {
            $('#msg').alert('close');
        }, 3000);
    }
});