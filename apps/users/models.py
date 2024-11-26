from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.utils import timezone

class User(AbstractUser):
    class UserRole(models.TextChoices):
        USER = "user", _("User")
        SALESMAN = "salesman", _("Salesman")

    role = models.CharField(_("Role"), choices=UserRole.choices, max_length=16)
    # phone_number = PhoneNumberField(max_length=13, null=True, blank=True)
    # user.phone_number struser.phone_number = +

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @staticmethod
    def create_fake_users(count=100):
        from faker import Faker
        import random
        
        fake = Faker()
        
        for _ in range(count):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = fake.unique.user_name()
            email = fake.unique.email()
            role = random.choice([User.UserRole.USER, User.UserRole.SALESMAN])

            User.objects.create_user(
                username=username,
                email=email,
                password="password123",  # Default password for all fake users
                first_name=first_name,
                last_name=last_name,
                role=role,
            )
        print(f"{count} fake users created successfully!")


class OneTimeCode(models.Model):
    code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return (timezone.now() - self.created_at).seconds > 60