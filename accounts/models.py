from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify


class Profile(models.Model):

    ACCOUNT_TYPES = (
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    account_type = models.CharField(
        max_length=15, choices=ACCOUNT_TYPES, default='tenant')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
