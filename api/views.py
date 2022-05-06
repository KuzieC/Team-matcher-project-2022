from rest_framework import viewsets
from teammatcherapp import models
from api.serializers import UserSerializer,LeaderboardSerializer,ItemsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from django.http import Http404

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    permission_classes = [DjangoModelPermissions]
    serializer_class = UserSerializer
class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = models.LeaderBoardPosition.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = LeaderboardSerializer
    def get_queryset(self, *args, **kwargs):
        owner_id = self.kwargs.get("user_pk")
        if (not owner_id == None):
            try:
                owner = models.User.objects.get(id=owner_id)
                return self.queryset.filter(username=owner.username)
            except models.User.DoesNotExist:
                raise Http404("User with that id does not exist")
        else:
            return self.queryset
class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.shopInfo.objects.all()
    permission_classes = [DjangoModelPermissions]
    serializer_class = ItemsSerializer
    def get_queryset(self, *args, **kwargs):
        owner_id = self.kwargs.get("user_pk")
        if (not owner_id == None):
            try:
                owner = models.User.objects.get(id=owner_id)
                return self.queryset.filter(owner=owner)
            except models.User.DoesNotExist:
                raise Http404("User with that id does not exist")
        else:
            return self.queryset
