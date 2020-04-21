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

DEVS = [
    (8888, 'emilte'),
    (9999, 'paskern'),
]

PASSWORD = "Django123"

class Command(BaseCommand):

    def confirmation(self):
        answer = None
        yes = ['yes', 'y']
        no = ['no', 'n']
        print("== This command will:")
        print("\t 1. Set following users as superuser:")
        for dev in DEVS:
            print(f"\t\t {dev[1]}")

        print("\n== Are you sure? DOUBLE-CHECK that this is not production server ==")

        while answer not in yes+no:
            answer = input("Type (Y)es or (N)o: ").lower()

        return answer in yes

    def f(self):
        # Set super devs for NICKNAMES:
        for dev in DEVS:
            user, created = User.objects.get_or_create(employee_nr=dev[0], nickname=dev[1])
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
