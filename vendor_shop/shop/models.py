from django.contrib.auth.models import AbstractUser
from django.db import models

class Vendor(AbstractUser):
    business_name = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='vendor_users',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='vendor_users',
        blank=True,
        help_text='Specific permissions for this user.'
    )




class Shop(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='shops')
    name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name