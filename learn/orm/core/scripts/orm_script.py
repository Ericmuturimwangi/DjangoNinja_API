from django.contrib.auth.models import User
from core.models import Restaurant, Rating
from django.utils import timezone
from django.db import connection

def run():
    restaurant = Restaurant.objects.first()
    user = User.objects.first()

    Rating.objects.create(user=user, restaurant=restaurant, rating = 3)

