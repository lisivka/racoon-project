from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import AuctionsModel

UserModel = get_user_model()


class AuctionsSerializers(ModelSerializer):
    class Meta:
        model = AuctionsModel
        fields = '__all__'
