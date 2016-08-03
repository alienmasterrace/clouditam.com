from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from dashboard.models import Asset, DashUser, Application

PAGE_TYPE = (
    ('Index', 'Index'),
    ('Pricing', 'Pricing'),
    ('Clients', 'Clients'),
    ('Contact', 'Contact'),
    ('About', 'About'),
)

PRICE_TYPE = (
    ('Monthly', 'Monthly'),
    ('Annually', 'Annually'),
    ('Free', 'Free')
)


class Settings(models.Model):
    maintenance_message = models.TextField()


class About(models.Model):
    pass


class Contact(models.Model):
    pass


class Client(models.Model):
    name = models.CharField(max_length=64, null=True)
    logo = models.ImageField(upload_to="clients", null=True)
    url = models.URLField(null=True)


class Account(models.Model):
    name = models.CharField(max_length=64, null=True)
    asset_limit = models.IntegerField(null=True, default=10, help_text="Give 0 for unlimited.")
    price = models.DecimalField(max_digits=64, decimal_places=2, null=True, default=0)
    details = RichTextField(null=True, config_name='awesome_ckeditor')
    type = models.CharField(max_length=64, default="Monthly", choices=PRICE_TYPE)


class Customer(models.Model):
    user = models.OneToOneField(User)
    assets = models.ManyToManyField(Asset,blank=True)
    users = models.ManyToManyField(DashUser,blank=True)
    apps = models.ManyToManyField(Application,blank=True)
    payment = models.OneToOneField("Payment",null=True,blank=True)
    plan_name = models.CharField(max_length=64, null=True)
    asset_limit = models.IntegerField(null=True, default=10)
    price = models.DecimalField(max_digits=64, decimal_places=2, null=True, default=0)
    details = RichTextField(null=True, config_name='awesome_ckeditor')
    type = models.CharField(max_length=64, default="Monthly", choices=PRICE_TYPE)


class Payment(models.Model):
    fullname = models.CharField(max_length=64, null=True, blank=True)
    company = models.CharField(max_length=64, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    state = models.CharField(max_length=64, null=True, blank=True)
    zip_or_postal = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)


class Header(models.Model):
    title = models.CharField(max_length=64, null=True)
    bg_image = models.ImageField(default="headers/default.jpg", upload_to="headers")
    text_area = RichTextField(config_name='awesome_ckeditor')
    button_text = models.CharField(max_length=64, null=True)
    button_url = models.CharField(max_length=64, null=True)
    page = models.CharField(max_length=64, choices=PAGE_TYPE, default="Index", unique=True)

    def __str__(self):
        return "{} Page".format(self.page)
