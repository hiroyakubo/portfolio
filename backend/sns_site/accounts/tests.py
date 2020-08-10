from django.test import TestCase

from .models import CustomUser


def create_user(username, email, age, photo):
    user = CustomUser(username=username, email=email, age=age, photo=photo)
    return user