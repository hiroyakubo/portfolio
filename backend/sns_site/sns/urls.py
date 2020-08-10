from django.urls import path

from . import views

urlpatterns = [
    path("", views.Top.as_view(), name="top"),
    path("home", views.Home.as_view(), name="home"),
    path("<str:user_name>", views.User_page.as_view(), name="user_page"),
    path("edit/<str:user_name>", views.Edit.as_view(), name="edit"),
    path("delete_tweet/<str:tweeter>/<int:tweet_id>", views.Delete_tweet.as_view(), name="delete_tweet"), 
    path("detail/<str:tweeter>/<int:tweet_id>", views.Tweet_detail.as_view(), name="tweet_detail"), 
    path("delete_comment/<str:tweeter>/<int:tweet_id>/<int:comment_id>", views.Delete_comment.as_view(), name="delete_comment"), 
]