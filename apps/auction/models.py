from django.contrib.auth import get_user_model
from django.db import models

from apps.lot.models import LotModel

UserModel = get_user_model()


class AuctionsModel(models.Model):
    class Meta:
        db_table = 'auctions_table'

    lot = models.ForeignKey(LotModel, on_delete=models.CASCADE, related_name='auctions')
    is_active = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
