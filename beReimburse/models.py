from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Employee(models.Model):
    name = models.TextField(max_length=100)
    nrek = models.CharField(max_length=100)
    #pswd = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    #admn = models.BooleanField()
class Reimburse(models.Model):
    date = models.DateField()
    desc = models.TextField(max_length=2000)
    amnt = models.PositiveIntegerField()
    rcpt = models.FileField(upload_to="")
    class Stats(models.TextChoices):
        ACCEPTED = 'ACC', _('Accepted')
        REJECTED = 'REJ', _('Rejected')
        ONHOLD   = 'ONH', _('Onhold')
        SUBMIT   = 'SBM', _('Submitted')
    stat = models.CharField(
        max_length=3, 
        choices=Stats.choices,
        default=Stats.SUBMIT,
    )
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, null=True)
