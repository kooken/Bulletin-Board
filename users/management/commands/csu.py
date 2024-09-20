from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@ads.com',
            first_name='Admin',
            last_name='Admin',
            role="admin",
            is_active=True,
        )

        user.set_password('12345')
        user.save()
