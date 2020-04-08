# imports
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core import management
# End: imports -----------------------------------------------------------------

# Settings:
USER_PW = "Django123"


class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            management.call_command('migrate')
            management.call_command('create_admin')
            # management.call_command('flush', interactive=False)
            management.call_command('myseed')
        except Exception as e:
            print(e)


        # End of handle
