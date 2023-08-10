from django.urls import path

from .views import *
urlpatterns = [
    path('', Land.as_view(), name="land"),
]
