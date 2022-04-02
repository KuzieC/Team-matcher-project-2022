from django.db import router
from django.urls import path
from api.views import UserViewSet
from rest_framework.routers import DefaultRouter

from teammatcherapp.models import User
router = DefaultRouter()
router.register('users',UserViewSet,basename = 'users')
router.register('leaderboardpositions',LeaderboardViewSet,basename = 'leaderboardpositions')
urlpatterns = router.urls 
