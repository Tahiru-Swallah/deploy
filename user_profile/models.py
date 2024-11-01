from django.db import models
from account.models import CustomUser

class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        related_name='profile',
        on_delete=models.CASCADE
    )
    profile_photo = models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True)


    def __str__(self):
        return f'{self.user.first_name}'