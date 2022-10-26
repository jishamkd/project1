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
    image = models.FileField(upload_to='customers/')
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=25)
    def __str__(self):
        return self.name


class manager(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='manager')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    image = models.FileField(upload_to='images/')
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=25)
    def __str__(self):
        return self.name

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
    user = models.ForeignKey(customer, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


class Assign_Work(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.DO_NOTHING)
    manager = models.ForeignKey(manager, on_delete=models.DO_NOTHING)
    cat = (('Two wheeler with gear', 'two wheeler with gear'),
           ('Two wheeler without gear','Two wheeler without gear'),
           ('Four wheeler','Four wheeler'),
           ('Three Wheeler','Three Wheeler'))
    category = models.CharField(max_length=50,choices=cat)
    vehicle_name = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_brand = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=10)
    problem_description = models.CharField(max_length=100)
    date = models.DateField()
    status = (('Repairing', 'Repairing'),
           ('Work Completed', 'Work Completed'),
              ('Payment Done', 'Payment Done')
           )
    rep_category = models.CharField(max_length=50,choices=status)
    cost = models.CharField(max_length=50,default=0)


class Payment(models.Model):
    Card_number = models.CharField(max_length=12)
    Expiry_Date = models.CharField(max_length=4)
    Cvv = models.CharField(max_length=3)


