from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

from .serializers import ProfileSerializer, UserSerializer

UserModel: User = get_user_model()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = UserModel.objects.exclude(pk=self.request.user.pk)
        return queryset


class UserProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile
