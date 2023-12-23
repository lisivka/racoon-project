from django.contrib.auth.models import User
from apps.users.models import UserModel
from django.core.management.base import BaseCommand, CommandError
import os
from dotenv import load_dotenv
load_dotenv()

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Command(BaseCommand):
    help = "Create superuser"

    def handle(self, *args, **options):
        try:
            email = os.getenv('DJANGO_SUPERUSER_EMAIL')
            password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

            if not UserModel.objects.filter(email=email).exists():
                is_active = True
                is_staff = True
                user = UserModel.objects.create_superuser(email=email, password=password, is_active=is_active, is_staff=is_staff)
                self.stdout.write(self.style.SUCCESS(f"Superuser '{email}' created successfully."))
            else:
                self.stdout.write(self.style.SUCCESS(f"Superuser '{email}' already exists."))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
            raise CommandError(f"Error: {e}")
