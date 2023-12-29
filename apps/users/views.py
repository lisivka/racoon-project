from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.models import Profile

from .serializers import ProfileSerializer, UserSerializer

User = get_user_model()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = User.objects.exclude(pk=self.request.user.pk)
        return queryset


class UserProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile
