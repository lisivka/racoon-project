from rest_framework.serializers import ModelSerializer

from .models import Auction
from  apps.lot.serializers import LotSerializers



class AuctionsSerializers(ModelSerializer):
    lot = LotSerializers()
    class Meta:
        model = Auction
        fields = '__all__'
