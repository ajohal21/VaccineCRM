from django.db import models

# Create your models here.


class Vaccine(models.Model):
    name = models.CharField(max_length=200)
    dose = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    vaccines = models.ManyToManyField(Vaccine)

class Vaccine_Timing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE) # This is the new line
    date_recieved = models.DateField()
    doses_recieved = models.IntegerField()




class Clinician(models.Model):
    name = models.CharField(max_length=200)
    clients = models.ManyToManyField(User)
