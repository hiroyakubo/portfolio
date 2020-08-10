from django.urls import path
from . import views


urlpatterns = [
    path('v1/like/', views.LikeView.as_view(), name='create_Like'),
]