from rest_framework.serializers import ModelSerializer

from .models import Auction
from  apps.lot.serializers import LotSerializer



class AuctionsSerializer(ModelSerializer):
    lot = LotSerializer()
    class Meta:
        model = Auction
        fields = '__all__'
