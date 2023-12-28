from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import LotModel, PhotoModel

UserModel = get_user_model()


class LotSerializer(ModelSerializer):
    class Meta:
        model = LotModel
        fields = "__all__"


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = "__all__"
