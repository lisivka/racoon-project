from rest_framework.serializers import ModelSerializer

from .models import Auction


class AuctionsSerializers(ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'
