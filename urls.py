from django.urls import path

from . import views

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('display-feed/', views.display_feed, name='display_feed'),
    path('fetch-rss/', views.fetch_rss_feed, name='fetch_rss_feed'),
]
