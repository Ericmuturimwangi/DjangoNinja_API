
from django.contrib import admin
from django.urls import path, include
from devices.api import app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', app.urls)
]
