from django.urls import path
from .views import index 

urlpatterns = [
    path('', index), #render the index template
    path('shop', index),
    path('leaderboard', index),
    path('search', index)
]
