from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


from common.models import TimeStampedModel
from .schemas import BidSchema

User = get_user_model()


class Bid(TimeStampedModel):
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='bid_user'
    )
    auction = models.ForeignKey(
        # TODO: add import Auction
        # Auction,
        verbose_name=_('auction'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='bid_auction'
    )
    bet = models.BigIntegerField(_('bet'))

    class Meta:
        verbose_name = _('bid')
        verbose_name_plural = _('bids')

    def save(self, *args, **kwargs):
        BidSchema.model_validate(self.__dict__)

        super().save(*args, **kwargs)
