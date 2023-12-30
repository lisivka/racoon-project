from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

User = get_user_model()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    ordering = ('created_at', )

    def get_queryset(self):
        queryset = User.objects.exclude(pk=self.request.user.pk)

        queryset = queryset.order_by(*self.ordering)

        return queryset
