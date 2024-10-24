from core.models import Restaurant
from django.utils import timezone
from django.db import connection

def run():

    restaurant = Restaurant.objects.first()
    print(restaurant)

    print (connection.queries)

