from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import TimeStamped

from ..auction.models import Auction

User = get_user_model()


class Bid(TimeStamped):
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='bid_user'
    )
    auction = models.ForeignKey(
        Auction,
        verbose_name=_('auction'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='bid_auction'
    )
    bet = models.BigIntegerField(_('bet'))

    class Meta:
        db_table = 'bid'
        verbose_name = _('bid')
        verbose_name_plural = _('bids')
