from django.contrib import admin
from .models import Tweet, Comment, Tweet_like, Comment_like


class TweetAdmin(admin.ModelAdmin):
    fields = [
        "user", 
        "tweet", 
    ]

class CommentAdmin(admin.ModelAdmin):
    fields = [
        "comment_item", 
        "user", 
        "tweet", 
    ]

class TweetLikeAdmin(admin.ModelAdmin):
    fields = [
        "tweet", 
        "user", 
        "ip_address", 
    ]
class CommentLikeAdmin(admin.ModelAdmin):
    fields = [
        "comment", 
        "user", 
        "ip_address", 
    ]

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tweet_like, TweetLikeAdmin)
admin.site.register(Comment_like, CommentLikeAdmin)