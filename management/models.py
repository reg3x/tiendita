import uuid as uuid
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampedModel(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    archived = models.DateTimeField()

    class Meta:
        abstract = True


class LocationInfo(models.Model):
    neighborhood = models.CharField(max_length=500, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.PositiveSmallIntegerField(max_length=2)
    state = models.PositiveSmallIntegerField(max_length=2)
    country = models.PositiveSmallIntegerField(max_length=3)

    class Meta:
        abstract = True


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(max_length=3)
    gender = models.PositiveSmallIntegerField(max_length=2)
    email = models.EmailField()
    phone = PhoneNumberField()
    cellphone = PhoneNumberField()
    instagram = models.CharField(max_length=50)

    class Meta:
        abstract = True


class UserAccount(TimeStampedModel, ContactInfo):
    """
    Application users: i.e: Admins or Customer with access to our app.
    """
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Contact(TimeStampedModel, ContactInfo):
    """
    Customer, Support from Provider, Shipping Contact, etc.
    """
    id = models.IntegerField(primary_key=True)
    account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True) # the contact has an account in our app


PLATFORM_TYPE_BROWSER = 0
PLATFORM_TYPE_ANDROID = 10
PLATFORM_TYPE_IOS = 20
PLATFORM_TYPE_CHOICES = (
    (PLATFORM_TYPE_BROWSER, "Web Client"),
    (PLATFORM_TYPE_BROWSER, "Android"),
    (PLATFORM_TYPE_BROWSER, "Iphone/Ipad"),
)


class PlatForm(models.Model):
    """
    The Platform used to contact/purchase. i.e: # Android, iOS, Browser, Instagram, WhatsApp.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.PositiveSmallIntegerField(max_length=2, choices=PLATFORM_TYPE_CHOICES)


class Operation(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    type = models.PositiveSmallIntegerField(max_length=2)  # Buy Sell Shipping
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    platform = models.ForeignKey(PlatForm, on_delete=models.CASCADE)
    amount = models.FloatField()


class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)


class ProductCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    target_gender = models.PositiveSmallIntegerField(max_length=1)
    target_age = models.PositiveSmallIntegerField(max_length=3)


class Product(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    cost = models.FloatField()
    sale_price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    categories = models.ManyToManyField(ProductCategory)
