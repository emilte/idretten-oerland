# imports
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core import management
from django.contrib.auth import get_user_model
import getpass
# End: imports -----------------------------------------------------------------

# Settings:

User = get_user_model()

EMAILS = [
    'emil.telstad@gmail.com',
    'stefan.pakaski@gmail.com',
]

PASSWORD = "Django123"

class Command(BaseCommand):

    def confirmation(self):
        answer = None
        yes = ['yes', 'y']
        no = ['no', 'n']
        print("== This command will:")
        print("\t 1. Set following users as superuser:")
        for email in EMAILS:
            print(f"\t\t {email}")

        print("\n== Are you sure? DOUBLE-CHECK that this is not production server ==")

        while answer not in yes+no:
            answer = input("Type 'y' or 'n': ").lower()

        return answer in yes

    def f(self):
        # Set super devs for EMAILS:
        for email in EMAILS:
            user, created = User.objects.get_or_create(email=email)
            user.is_staff = True
            user.is_superuser = True
            user.set_password(PASSWORD)
            user.save()
        # End: f


    def handle(self, *args, **options):
        print("\n== COMMAND: sudev ==")
        if self.confirmation():
            self.f()
        else:
            print("== ABORT ==")
        # End of handle
