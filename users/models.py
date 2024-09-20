from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choices = (
        (USER, USER),
        (ADMIN, ADMIN),
    )


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    first_name = models.CharField(
        max_length=64,
        verbose_name="Name",
        help_text="Enter your name here",
    )

    last_name = models.CharField(
        max_length=64,
        verbose_name="Surname",
        help_text="Enter your surname here",
    )

    email = models.EmailField(
        "email address",
        unique=True,
        help_text="Enter your email here",
    )

    phone = PhoneNumberField(
        verbose_name="Phone number",
        help_text="Enter your phone number here",

    )

    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="User role",
        help_text="Enter users' role here",
    )

    image = models.ImageField(
        upload_to="photos/",
        verbose_name="avatar",
        help_text="Attach your avatar here",
        **NULLABLE,
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Active status",
        help_text="Is your status active?"
    )

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
