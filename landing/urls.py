from django.urls import path

from .views import *
urlpatterns = [
    path('', Land.as_view(), name="land"),
    path('about/', About.as_view(), name="about"),
    path('apply/', Apply.as_view(), name="apply"),
    path('research/', ResearchView.as_view(), name="research"),
    path('contact/', Contact.as_view(), name="contact"),
    path('subjects/', Study.as_view(), name="study"),
    path('research/<str:pk>/', ResearchDetail.as_view(), name="research-detail"),
]
