from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth import get_user_model

from .models import Bid

User = get_user_model()


class AuctionBidConsumer(AsyncJsonWebsocketConsumer):
    ordering = ('-created_at', )

    @database_sync_to_async
    def get_bids(self, auction_id):
        return Bid.objects.get(id=auction_id)

    async def connect(self):
        self.auction_id = self.scope['url_route']['kwargs']['auction_pk']
        self.auction_group_name = f'auction_{self.auction_id}'

        await self.channel_layer.group_add(
            self.auction_group_name,
            self.channel_name,
        )

        await self.accept()

