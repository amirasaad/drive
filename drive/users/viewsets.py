
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from drive.users.permissions import IsAuthenticatedOrCreate
from drive.users.serializers import UserSerializer

User = get_user_model()


class UsersViewSet(
        GenericViewSet,
        mixins.CreateModelMixin):
    """
    Api endpoint for signup a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrCreate]
