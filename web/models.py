from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

PAGE_TYPE = (
    (1, 'Index'),
    (2, 'Pricing'),
    (3, 'Clients'),
    (4, 'Contact'),
    (5, 'About'),
)

PRICE_TYPE = (
    (1, 'Monthly'),
    (2, 'Annually')
)


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
    price = models.FloatField(null=True, default=0)
    details = RichTextField(null=True,config_name='awesome_ckeditor')
    type = models.IntegerField(default=1, choices=PRICE_TYPE)


class Customer(models.Model):
    account = models.ForeignKey(Account)
    user = models.OneToOneField(User, unique=True)


class Header(models.Model):
    title = models.CharField(max_length=64,null=True)
    bg_image = models.ImageField(default="headers/default.jpg", upload_to="headers")
    text_area = RichTextField(config_name='awesome_ckeditor')
    button_text = models.CharField(max_length=64,null=True)
    button_url = models.CharField(max_length=64, null=True)
    page = models.IntegerField(choices=PAGE_TYPE,default=1, unique=True)

    def __str__(self):
        return "{} Page".format(PAGE_TYPE[self.page-1][1])