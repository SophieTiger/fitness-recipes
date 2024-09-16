$(document).ready(function() {
    // Add CSRF token to all AJAX requests
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            }
        }
    });
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
                showMessage(data.message, 'success');
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

    function showMessage(message, type) {
        var alertClass = type === 'success' ? 'alert-success' : 'alert-danger';
        var messageHtml = `
            <div class="alert ${alertClass} alert-dismissible fade show" id="msg" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
        messageContainer.html(messageHtml);
    
        // Clear the message from Django's message storage
        $.ajax({
            url: '/recipes/clear-messages/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                console.log('Messages cleared');
            },
            error: function(xhr, status, error) {
                console.error('Error clearing messages:', error);
            }
        });
    }
});