from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth import get_user_model
from django.db import close_old_connections
from django.db.models import Max
from pydantic import ValidationError

from apps.bid.serializers import BidSerializer
from services.jwt_authenticator import JWTAuthenticator

from .models import Bid

User = get_user_model()


class AuctionBidConsumer(AsyncJsonWebsocketConsumer):
    ordering = ('-created_at', )

    @database_sync_to_async
    def get_auction_list(self):
        return Bid.objects.filter(auction_id=self.auction_id).order_by(*self.ordering)

    @database_sync_to_async
    def get_max_bed(self):
        max_bid = Bid.objects.filter(auction_id=self.auction_id).aggregate(Max('bet'))
        return max_bid['bet__max'] or 0

    @database_sync_to_async
    def create_bid(self, bet):
        return Bid.objects.create(user_id=self.scope['user'].id, auction_id=self.auction_id, bet=bet)

    @staticmethod
    @sync_to_async
    def get_validate_data(instance):
        try:
            return BidSerializer(instance).data
        except Exception as error:
            raise ValidationError({"error": str(error)}) from error

    async def connect(self):
        self.auction_id = self.scope['url_route']['kwargs']['auction_pk']
        self.user_group_name = f'auction_{self.auction_id}'

        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name,
        )

        await self.accept()

    async def receive_json(self, content, **kwargs):
        try:
            access_token = content.get('accessToken', None)
            bid_create = content.get('bidCreate', None)

            await self.is_authenticated_or_disconnect(access_token)

            if access_token:
                await self.send_bid_list()
            elif bid_create:
                bet = content.get('bet', None)
                if bet:
                    bet = int(bet)

                    if not isinstance(bet, int) or bet <= 0:
                        raise ValueError("Bet must be a positive integer.")

                    max_bet = await self.get_max_bed()
                    if bet <= max_bet:
                        raise ValueError("Bet must be greater than the current maximum bid.")

                    try:
                        new_bid = await self.create_bid(bet)
                        bid_dict = await self.get_validate_data(new_bid)
                        bid_dict['type'] = 'send_create_bid'

                        await self.channel_layer.group_send(
                            self.user_group_name,
                            bid_dict,
                        )

                    except Exception as error:
                        await self.send_json({"error": str(error)})

                else:
                    await self.send_json({"error": "Missing 'bet' in bid creation data."})

        except ValueError as error:
            await self.send_json({"error": str(error)})
        except Exception as error:
            await self.send_json({"error": str(error)})

    async def send_bid_list(self):
        try:
            queryset = await self.get_auction_list()
            bids_data = [await self.get_validate_data(bid) async for bid in queryset]

            await self.send_json({
                'bids': bids_data,
            })

        except Exception as error:
            await self.send_json({"error": str(error)})

    async def send_create_bid(self, event):
        try:
            bid_dict = event
            bid_dict['create'] = True

            await self.send_json(bid_dict)
        except Exception as error:
            await self.send_json({"error": str(error)})

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.user_group_name,
            self.channel_name,
        )

    async def is_authenticated_or_disconnect(self, access_token=None):
        if access_token:
            user = await JWTAuthenticator(access_token).get_user_from_token()
            self.scope['user'] = user
            await sync_to_async(self.scope['user'].save)()
            close_old_connections()

        if self.scope['user'].is_authenticated:
            return True

        await self.disconnect(4401)
