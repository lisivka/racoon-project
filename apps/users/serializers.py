from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.serializers import CharField, ModelSerializer, ValidationError

from apps.users.models import Profile
from racoon_project.settings import DEFAULT_USER_AVATAR_URL, USER_AVATAR_MAX_SIZE_MB

User = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'phone', 'avatar')

    @staticmethod
    def validate_avatar(value):
        if value and value.size > (USER_AVATAR_MAX_SIZE_MB * 1024 * 1024):
            raise ValidationError(f'Maximum image size allowed is {USER_AVATAR_MAX_SIZE_MB} Mb')
        return value


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=False)
    confirm_password = CharField(write_only=True, required=False)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id', 'email', 'password', 'confirm_password', 'is_active', 'is_staff', 'is_superuser', 'last_login',
            'created_at', 'updated_at', 'profile'
        )

    @transaction.atomic
    def create(self, validated_data: dict):
        # extract the fields from validated_data or set it to None if absent
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)

        # check that the 'password' field is not empty
        if password is None:
            raise ValidationError(
                {'password': 'Password is required for user creation.'}
            )

        # check that the 'password' matches the 'confirm_password' field
        if password != confirm_password:
            raise ValidationError(
                {'confirm_password': 'Password and confirm_password are different.'}
            )

        profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data, password=password)
        Profile.objects.create(**profile, user=user)

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})

        if self.context['request'].data.get('profile.avatar') == '':
            instance.profile.avatar = None
            instance.save()

        profile_serializer = ProfileSerializer(instance.profile, data=profile_data, partial=True)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        # Initialize the data dictionary with the default representation
        data = super().to_representation(instance)

        if hasattr(instance.profile, 'avatar') and instance.profile.avatar and hasattr(instance.profile.avatar, 'file'):
            data['profile']['avatar'] = instance.profile.avatar.url
        else:
            # if the image does not exist, we send the image for the user by default
            data['profile']['avatar'] = DEFAULT_USER_AVATAR_URL

        return data

    @staticmethod
    def validate_email(value):
        if not value:
            raise ValidationError('Email field is required.')
        # check that the email field is not use
        if User.objects.filter(email=value).exists():
            raise ValidationError('Email is already in use.')

        return value
