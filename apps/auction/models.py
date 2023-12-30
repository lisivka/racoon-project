from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.lot.models import Lot
from common.enums import AuctionStatus
from common.models import TimeStamped


class Auction(TimeStamped):
    lot = models.ForeignKey(Lot, on_delete=models.SET_NULL, null=True, related_name='auction')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        _('status'),
        choices=[(status.name, status.value) for status in AuctionStatus],
        default=AuctionStatus.PENDING.value,
        max_length=20
    )

    class Meta:
        db_table = 'auction'
        verbose_name = _('auction')
        verbose_name_plural = _('auctions')
