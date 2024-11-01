from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
import random
class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        if not email and not phone_number:
            raise ValueError('The user must have either email address or phone number')
        if email:
            email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, phone_number, password, **extra_fields)
    
class CustomUser(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email or self.phone_number


class Code(models.Model):
    number = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.number)
    
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = ''.join(str(item) for item in code_items)
        self.number = code_string
        super().save(*args, **kwargs)