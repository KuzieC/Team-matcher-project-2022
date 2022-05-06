from django.db import router
from django.urls import path, include, re_path
from api.views import UserViewSet,LeaderboardViewSet,ItemViewSet
from rest_framework.routers import DefaultRouter

from teammatcherapp.models import User
router = DefaultRouter()
router.register('users',UserViewSet,basename = 'users')
router.register('leaderboardpositions',LeaderboardViewSet,basename = 'leaderboardpositions')
router.register('items',ItemViewSet,basename = 'items')
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^users/(?P<user_pk>\d+)/items/?$', ItemViewSet.as_view({'get':'list'}), name='user-items-list'),
    re_path(r'^users/(?P<user_pk>\d+)/items/(?P<pk>\d+)/?$', ItemViewSet.as_view({'get':'retrieve'}), name='user-item-detail'),
    re_path(r'^users/(?P<user_pk>\d+)/leaderboardpositions/?$', LeaderboardViewSet.as_view({'get':'list'}), name='user-leaderboard-list'),
    ]
