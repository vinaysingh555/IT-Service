import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from application.custom_models import DateTimeModel
from apps.service.models import Service
from apps.user.manager import CustomUserManager


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    first_name = models.CharField('First name', max_length=30, blank=True)
    last_name = models.CharField('Last name', max_length=150, blank=True)
    username = models.EmailField(
        'username', unique=True, help_text='Username.', null=True
    )
    email = models.EmailField(
        'Email address', unique=True, help_text='Email address.', null=True
    )
    objects = CustomUserManager()

    class Meta:
        ordering = ('-date_joined',)

    def __str__(self):
        return self.email if self.email else str(self.id)


class Profile(DateTimeModel):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        if self.user:
            return self.user.first_name + ' ' + self.user.last_name if self.user.first_name and self.user.last_name  else self.user.email
        else:
            return str(self.id)

class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)



class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,null=True)
    subscription_date = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=50)

    def _str_(self):
        return f"Subscription by {self.user} for {self.service}"



