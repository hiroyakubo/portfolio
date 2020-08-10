from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from accounts.models import CustomUser
from .models import Tweet, Comment, Tweet_like, Comment_like

class TweetModelTests(TestCase):
    def test_tweet_english(self):
        tweet = Tweet(tweet="test_case")
        self.assertEqual(tweet.tweet, "test_case")

    def test_tweet_japanese(self):
        tweet = Tweet(tweet="テストケース")
        self.assertEqual(tweet.tweet, "テストケース")

    def test_tweet_number(self):
        tweet = Tweet(tweet="123")
        self.assertEqual(tweet.tweet, "123")

    def test_tweet_empty(self):
        tweet = Tweet(tweet="")
        self.assertEqual(tweet.tweet, "")

class CommentModelTests(TestCase):
    def test_comment_english(self):
        comment = Comment(comment_item="test_case")
        self.assertEqual(comment.comment_item, "test_case")

    def test_comment_japanese(self):
        comment = Comment(comment_item="テストケース")
        self.assertEqual(comment.comment_item, "テストケース")

    def test_comment_number(self):
        comment = Comment(comment_item="123")
        self.assertEqual(comment.comment_item, "123")

    def test_comment_empty(self):
        comment = Comment(comment_item="")
        self.assertEqual(comment.comment_item, "")

class TopViewTest(TestCase):
    def test_get_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, "sns/top_base.html")

class SignupViewTest(TestCase):
    def test_get_success(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        
class LoginViewTest(TestCase):
    def test_get_success(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)