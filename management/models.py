from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampedModel(models):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    archived = models.DateTimeField()


class LocationInfo(models):
    neighborhood = models.CharField(max_length=500, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.PositiveSmallIntegerField()
    state = models.PositiveSmallIntegerField()
    country = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True


class ContactInfo(models):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(max_length=3)
    sex = models.PositiveSmallIntegerField(max_length=2)
    email = models.EmailField()
    phone = PhoneNumberField()
    cellphone = PhoneNumberField()
    instagram = models.CharField(max_length=50)

    class Meta:
        abstract = True


class UserAccount(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Contact(models):
    id = models.IntegerField(primary_key=True)

