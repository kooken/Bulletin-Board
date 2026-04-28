from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "Create a default superuser for development"

    def handle(self, *args, **options):
        if User.objects.filter(email="admin@ads.com").exists():
            self.stdout.write("Superuser already exists.")
            return

        User.objects.create_superuser(
            email="admin@ads.com",
            first_name="Admin",
            last_name="Admin",
            phone="+10000000000",
            password="admin",
        )
        self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
