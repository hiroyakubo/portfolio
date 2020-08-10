import os

from django.shortcuts import render, redirect, reverse
from django.views import View

from config.settings import MEDIA_ROOT, MEDIA_URL
from accounts.models import CustomUser
from .models import Tweet, Comment, Tweet_like, Comment_like
from .forms import UsernameForm, EmailForm, ProfileForm, TweetForm, CommentForm


def get_image_path(user):
    if user.photo.name == "":
        img = os.path.join(MEDIA_URL, "profile/nonsetting.png")
    else:
        img = os.path.join(MEDIA_URL, user.photo.name)
    return img

class Top(View):
    def get(self, request, *args, **kwargs):
        context = {"messege": "none"}

        return render(request, "sns/top.html", context)

class Home(View):
    def get(self, request, *args, **kwargs):
        context = {
            "user": request.user.username, 
            "tweet_list": [{
                "obj": x, 
                "photo": get_image_path(CustomUser.objects.get(email=x.user)), 
                "like": int(Tweet_like.objects.filter(tweet_id=x.pk).count()), 
                } for x in Tweet.objects.all()][::-1], 
        }

        return render(request, "sns/home.html", context)

class User_page(View):
    def get(self, request, user_name, *args, **kwargs):
        user = CustomUser.objects.get(username=user_name)
        age = user.age if user.age is not None else "設定されていません"
        is_the_person = user == request.user
        tweet_form = TweetForm()
        img = get_image_path(user)

        context = {
            "user": user, 
            "age": age, 
            "photo": img, 
            "is_the_person": is_the_person, 
            "is_anonymous": request.user.is_anonymous, 
            "tweet_form": tweet_form, 
            "tweet_list": [{
                "message": x.tweet, 
                "id": x.pk, 
                "like": int(Tweet_like.objects.filter(tweet_id=x.pk).count()), 
                } for x in Tweet.objects.filter(user=user)][::-1], 
        }

        return render(request, "sns/user_page.html", context)
    
    def post(self, request, user_name, *args, **kwargs):
        tweet_form = TweetForm(request.POST)
        if tweet_form.is_valid():
            form = tweet_form.save(commit=False)
            form.user = request.user
            form.save()
        
        return redirect(reverse("user_page", kwargs={"user_name": user_name}))

class Edit(View):
    def get(self, request, user_name, *args, **kwargs):
        user = CustomUser.objects.get(username=user_name)
        img = get_image_path(user)

        username_form = UsernameForm(
            initial={
                "username": user.username
            }
        )
        email_form = EmailForm(
            initial={
                "email": user.email
            }
        )
        profile_form = ProfileForm(
            initial={
            "age": user.age, 
            "photo": user.photo, 
            })

        context = {
            "username_form": username_form, 
            "email_form": email_form, 
            "profile_form": profile_form, 
            "user": user.username, 
            "photo": img, 
        }

        return render(request, "sns/edit.html", context)

    def post(self, request, user_name, *args, **kwargs):
        username_form = UsernameForm(request.POST, request.FILES)
        email_form = EmailForm(request.POST, request.FILES)
        profile_form = ProfileForm(request.POST, request.FILES)
        user = CustomUser.objects.get(username=user_name)

        if username_form.is_valid():
            user.username = request.POST["username"]
            user.save()
        
        if email_form.is_valid():
            user.email = request.POST["email"]
            user.save()

        if profile_form.is_valid():
            user.age = request.POST["age"]

            if "photo" in request.FILES:
                os.remove(os.path.join(MEDIA_ROOT, user.photo.name))
                user.photo = request.FILES["photo"]
            user.save()
        
        return redirect(reverse("edit", kwargs={"user_name": user_name}))

class Tweet_detail(View):
    def get(self, request, tweeter, tweet_id, *args, **kwargs):
        item = Tweet.objects.get(id=tweet_id).tweet
        user = CustomUser.objects.get(username=tweeter)
        img = get_image_path(user)

        context = {
            "tweeter": tweeter, 
            "tweet_item": item, 
            "user": user, 
            "comment_form": CommentForm(), 
            "is_anonymous": request.user.is_anonymous, 
            "request_user": request.user, 
            "img_path": img, 
            "comment_list": [{
                "comment": x, 
                "photo": get_image_path(x.user), 
                } for x in Comment.objects.filter(tweet=Tweet.objects.get(pk=tweet_id))], 
        }

        return render(request, "sns/detail.html", context)
    
    def post(self, request, tweeter, tweet_id, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.user = CustomUser.objects.get(email=request.user)
            form.tweet = Tweet.objects.get(pk=tweet_id)
            form.save()

        return redirect(reverse("tweet_detail", kwargs={"tweeter": tweeter, "tweet_id": tweet_id}))

class Delete_tweet(View):
    def get(self, request, user_id, tweet_id, *args, **kwargs):
        r = Tweet.objects.filter(pk=tweet_id)
        r.delete()

        return redirect(reverse("user_page", kwargs={"user_name": request.user.username}))

class Delete_comment(View):
    def get(self, request, tweeter, tweet_id, comment_id, *args, **kwargs):
        c = Comment.objects.filter(pk=comment_id)
        c.delete()

        return redirect(reverse("recruit_detail", kwargs={"tweeter": tweeter, "tweet_id": tweet_id}))
