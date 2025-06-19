from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    vaccines = models.ManyToManyField(Vaccine)


class Clinician(models.Model):
    name = models.CharField(max_length=200)
    clients = models.ManyToManyField(User)


class Vaccine(models.Model):
    name = models.CharField(max_length=200)
    date_recieved = models.DateField()
    doses_recieved = models.IntegerField()
