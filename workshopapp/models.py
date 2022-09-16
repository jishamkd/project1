from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models


class Login(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class customer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='customer')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=300)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=25)

class manager(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='manager')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=25)

class feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    date = models.DateField()
    feedback = models.CharField(max_length=500)
    reply = models.CharField(max_length=500, null=True, blank=True)


class Manager_Contact_Admin(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    message = models.CharField(max_length=500)
    reply = models.CharField(max_length=500, null=True, blank=True)



class Schedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    user = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)




