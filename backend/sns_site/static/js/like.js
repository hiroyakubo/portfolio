$(function(){
    // setup for ajax
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // いいねボタン押下時の処理
    onClickVoteButton();

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function onClickVoteButton() {
        $('.like-button').on('click', function() {
            var tweetId = $(this).data('tweet-id');
            var commentId = $(this).data('comment-id');
            var currentCount = $(this).data('count');
            var countViewer = $(this).find('.like-counter');

            vote(tweetId, commentId, currentCount, countViewer);
        });
    }

    // ajax通信して投票結果を反映する
    function vote(tweetId, commentId, currentCount, countViewer) {
        let url = '/api/v1/like/';
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                comment_id: commentId, 
                tweet_id: tweetId, 
            }
        }).then(
            data => {
                if (data.result) {
                    currentCount = data["countNum"];
                    countViewer.text(currentCount);
                }
            },
            error => {
                if (error.responseJSON.message) {
                    alert(error.responseJSON.message);
                }
            }
        );
    }
});