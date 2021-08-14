from django.urls import path
from .views import show_news

urlpatterns = [
    path('index',show_news)
]