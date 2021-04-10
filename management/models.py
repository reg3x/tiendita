import uuid as uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
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
    city = models.PositiveSmallIntegerField()
    state = models.PositiveSmallIntegerField()
    country = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    gender = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Contact(TimeStampedModel, ContactInfo):
    """
    Customer, Support from Provider, Shipping Contact, etc.
    """
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.PositiveSmallIntegerField(choices=PLATFORM_TYPE_CHOICES)


class Operation(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    type = models.PositiveSmallIntegerField()  # Buy Sell Shipping
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    platform = models.ForeignKey(PlatForm, on_delete=models.CASCADE)
    amount = models.FloatField()


class Brand(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)


class ProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    target_gender = models.PositiveSmallIntegerField()
    target_age = models.PositiveSmallIntegerField()


class Product(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    cost = models.FloatField()
    sale_price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    categories = models.ManyToManyField(ProductCategory)
