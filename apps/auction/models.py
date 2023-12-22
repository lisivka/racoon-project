from django.contrib.auth import get_user_model
from django.db import models

from core.enums.auction_status_enum import AuctionStatusEnum
from lot.models import LotModel

UserModel = get_user_model()


class AuctionsModel(models.Model):
    class Meta:
        db_table = 'auctions_table'

    lot_id = models.ForeignKey(LotModel, on_delete=models.CASCADE, related_name='auctions')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auctions')

    is_active = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=[(status.value, status) for status in AuctionStatusEnum],
                              default=AuctionStatusEnum.Close.value, null=True)

    start_date = models.DateField(null=True)
    current_bid = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='bet')
