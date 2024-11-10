from django.db import models
from django.conf import settings
import uuid

class Withdraw(models.Model):
    STATUS_CHOICES = (
        ('1', 'Pending'),
        ('2', 'Reject'),
        ('3', 'Complete')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.FloatField()
    crypto_name = models.CharField(max_length=50)
    amount_game_token = models.FloatField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'withdraws'
        verbose_name = 'Withdraw'
        verbose_name_plural = 'Withdraws'


class Deposit(models.Model):
    STATUS_CHOICES = (
        ('1', 'Pending'),
        ('2', 'Reject'),
        ('3', 'Complete')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.FloatField()
    crypto_name = models.CharField(max_length=50)
    amount_game_token = models.FloatField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'deposits'
        verbose_name = 'Deposit'
        verbose_name_plural = 'Deposits'