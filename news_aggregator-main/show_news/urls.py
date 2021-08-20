from django.urls import path
from .views import show_news

urlpatterns = [
    path('',show_news)
]