from django.db import models

from accounts.models import CustomUser


class Tweet(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
    )
    tweet = models.CharField(
        max_length=300, 
        verbose_name="投稿", 
    )

class Comment(models.Model):
    comment_item = models.CharField(
        max_length=300, 
        verbose_name="コメント", 
    )
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
    )
    tweet = models.ForeignKey(
        Tweet, 
        on_delete=models.CASCADE, 
    )

class Tweet_like(models.Model):
    tweet = models.ForeignKey(
        Tweet, 
        on_delete=models.CASCADE, 
    )
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
    )

class Comment_like(models.Model):
    comment = models.ForeignKey(
        Comment, 
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
    )