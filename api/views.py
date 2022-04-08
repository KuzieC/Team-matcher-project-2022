from rest_framework import viewsets
from teammatcherapp import models
from api.serializers import UserSerializer,LeaderboardSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    permission_classes = [DjangoModelPermissions]
    serializer_class = UserSerializer
class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = models.LeaderBoardPosition.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = LeaderboardSerializer
