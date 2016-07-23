from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
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
    logo = models.ImageField(upload_to="clients",null=True)
    url = models.URLField(null=True)


class Account(models.Model):
    name = models.CharField(max_length=64, null=True)
    asset_limit = models.IntegerField(null=True, default=10,help_text="Give 0 for unlimited.")
    price = models.DecimalField(max_digits=64, decimal_places=2, null=True, default=0)
    details = RichTextField(null=True,config_name='awesome_ckeditor')
    type = models.CharField(max_length=64,default="Monthly", choices=PRICE_TYPE)


class Customer(models.Model):
    address = models.TextField()
    account = models.ForeignKey(Account)
    user = models.OneToOneField(User, unique=True)
    assets = models.ManyToManyField(Asset)
    users = models.ManyToManyField(DashUser)
    apps = models.ManyToManyField(Application)


class Header(models.Model):
    title = models.CharField(max_length=64,null=True)
    bg_image = models.ImageField(default="headers/default.jpg", upload_to="headers")
    text_area = RichTextField(config_name='awesome_ckeditor')
    button_text = models.CharField(max_length=64,null=True)
    button_url = models.CharField(max_length=64, null=True)
    page = models.CharField(max_length=64, choices=PAGE_TYPE,default="Index", unique=True)

    def __str__(self):
        return "{} Page".format(self.page)