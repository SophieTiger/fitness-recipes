$(document).ready(function() {
    // Define variables
    const likeButtons = $('.like-button');
    const messageContainer = $('.col-md-8.offset-md-2');

    likeButtons.click(function(e) {
        e.preventDefault();  // Prevent the default form submission
        var form = $(this).closest('form');
        var button = $(this);  // Store reference to the clicked button
        var likesCountElement = button.siblings('#likes-count');
        var currentLikes = parseInt(likesCountElement.text());
        var isCurrentlyLiked = button.find('i').hasClass('fas');

        // Immediate (optimistic) update
        if (isCurrentlyLiked) {
        button.find('i').removeClass('fas liked-heart').addClass('far unliked-heart');
        updateLikesCount(likesCountElement, currentLikes - 1);
        } else {
        button.find('i').removeClass('far unliked-heart').addClass('fas liked-heart');
        updateLikesCount(likesCountElement, currentLikes + 1);
        }
        
        $.ajax({
            url: form.attr('action'),
            type: 'POST',
            data: form.serialize(),
            dataType: 'json',
            success: function(data) {
                // Update with actual server data if it's different
                if (data.liked !== isCurrentlyLiked) {
                    if (data.liked) {
                    button.find('i').removeClass('far unliked-heart').addClass('fas liked-heart');
                    } else {
                    button.find('i').removeClass('fas liked-heart').addClass('far unliked-heart');
                    }
                }
                if (data.likes_count !== currentLikes) {
                    updateLikesCount(likesCountElement, data.likes_count);
                }
                
                // Display the message
                showMessage(data.message);
            },
            error: function(xhr, status, error) {
                // Revert optimistic update on error
                if (isCurrentlyLiked) {
                    button.find('i').removeClass('far unliked-heart').addClass('fas liked-heart');
                } else {
                button.find('i').removeClass('fas liked-heart').addClass('far unliked-heart');
                }
                updateLikesCount(likesCountElement, currentLikes);
                console.error("An error occurred: " + error);
                showMessage("An error occurred while processing your request.");
            }
        });
    });

    function updateLikesCount(element, newCount) {
        element.text(newCount)
               .addClass('highlight')
               .delay(300)
               .queue(function(next){
                   $(this).removeClass('highlight');
                   next();
               });
    }

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