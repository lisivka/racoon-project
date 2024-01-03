import traceback

from channels.db import database_sync_to_async
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from jwt import DecodeError, ExpiredSignatureError, InvalidSignatureError
from jwt import decode as jwt_decode

User = get_user_model()


class JWTAuthenticator:
    """
    JWT token authorization
    """
    def __init__(self, jwt_token=None):
        self.jwt_token = jwt_token

    async def get_user_from_token(self):
        try:
            if self.jwt_token:
                jwt_payload = JWTAuthenticator.get_payload(self.jwt_token)
                user_credentials = JWTAuthenticator.get_user_credentials(jwt_payload)
                user = await JWTAuthenticator.get_logged_in_user(user_credentials)
                return user
            else:
                return AnonymousUser()
        except (InvalidSignatureError, KeyError, ExpiredSignatureError, DecodeError):
            traceback.print_exc()
            return AnonymousUser()

    @staticmethod
    def get_payload(jwt_token):
        payload = jwt_decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload

    @staticmethod
    def get_user_credentials(payload):
        """
        method to get user credentials from jwt token payload.
        defaults to user id.
        """
        user_id = payload['user_id']
        return user_id

    @staticmethod
    async def get_logged_in_user(user_id):
        user = await JWTAuthenticator.get_user(user_id)
        return user

    @staticmethod
    @database_sync_to_async
    def get_user(user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return AnonymousUser()
