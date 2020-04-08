# imports
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core import management
from accounts.models import *
# End: imports -----------------------------------------------------------------

# Settings:
USER_PW = "Django123"


class Command(BaseCommand):

    def createsu(self):
        email = "admin@admin.com"
        User.objects.create_superuser(
            email=email,
            password=USER_PW,
            nickname="admin",
            first_name="Admin",
            last_name="Adminsen",
        )


    def handle(self, *args, **options):
        try:
            self.createsu()
        except Exception as e:
            print(e)
        # End of handle
