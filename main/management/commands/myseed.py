# imports
from django_seed import Seed
from faker import Faker
import random

from django.utils import timezone
from django.core import management
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from emil import models as emil_models

# End: imports -----------------------------------------------------------------

# OBS: seed() on instance was depricated for Faker module.
# Manually edited django-seed module __init__.py on line 35 from seed to seed_instance

# Settings:
User = get_user_model()

class Command(BaseCommand):

    def i(self, x, y):
        return random.randint(x, y)

    def fake_rgba(self, x=0, y=255):
        r, g, b, a = self.i(x,y), self.i(x,y), self.i(x,y), random.choice([0.6, 0.7, 0.8, 0.9, 1])
        return f"rgba({r},{g},{b},{a})"

    def f(self):
        seeder = Seed.seeder()

        seeder.faker.seed_instance(1234)

        seeder.add_entity(User, 20, {
            'department': lambda x: seeder.faker.word(),
        })
        seeder.add_entity(emil_models.Workout, 200, {
            'distance': lambda x: round(random.uniform(0, 20), 1),
            'type': lambda x: random.randint(0, 6),
            'comment': lambda x: seeder.faker.sentence(nb_words=2),
            'date': lambda x: seeder.faker.date_this_year(after_today=False),
        })

        seeder.execute()



    def handle(self, *args, **options):
        self.f()
        # End of handle
