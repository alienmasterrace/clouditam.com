from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

CURRENCIES = (
    ("$", "$"),
)

COUNTRIES = (
    ("Turkey", "Turkey"),
)

CATEGORY_TYPES = (
    ("Asset", "Asset"),
)

MEMORY_TYPES = (
    ("TB", "TB"),
    ("GB", "GB"),
    ("MB", "MB"),
)

PLATFORMS = (
    ("Physical", "Physical"),
)


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, null=True)


class Company(models.Model):
    name = models.CharField(max_length=64, null=True)


class Location(models.Model):
    name = models.CharField(max_length=64, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    location_currency = models.CharField(null=True, max_length=64, choices=CURRENCIES)
    address = models.TextField(null=True)
    city = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=64, null=True)
    postal_code = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=64, null=True, choices=COUNTRIES)


class Supplier(models.Model):
    name = models.CharField(max_length=64, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=64, null=True)
    postal_code = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=64, null=True, choices=COUNTRIES)
    contact_name = models.CharField(max_length=64, null=True)
    phone_number = PhoneNumberField(blank=True)
    fax_number = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    url = models.URLField(blank=True)
    notes = models.TextField(null=True)
    image = models.ImageField(upload_to="suppliers")


class Category(models.Model):
    name = models.CharField(max_length=64, null=True)
    type = models.CharField(max_length=64, null=True, choices=CATEGORY_TYPES)


class Application(models.Model):
    pass


class Hardware(models.Model):
    manufacturer = models.ForeignKey("Manufacturer")
    category = models.ForeignKey("Category")
    model = models.CharField(max_length=64, null=True)
    notes = models.TextField(null=True)
    image = models.ImageField(upload_to="suppliers")


class Asset(models.Model):
    name = models.CharField(max_length=64, null=True)
    memory_size = models.DecimalField(max_digits=64, decimal_places=2, null=True, default=0)
    memory_type = models.CharField(max_length=64, null=True, choices=MEMORY_TYPES)
    cpu_speed = models.DecimalField(max_digits=64, decimal_places=2, null=True, default=0)
    cpu_count = models.IntegerField(null=True, default=0)
    disk_size = models.DecimalField(max_digits=64, decimal_places=2, null=True, default=0)
    disk_type = models.CharField(max_length=64, null=True, choices=MEMORY_TYPES)
    ip_address = models.GenericIPAddressField(null=True)
    role = models.CharField(max_length=64, null=True)
    platform = models.CharField(max_length=64, null=True, choices=PLATFORMS)
    serial = models.CharField(max_length=64, null=True)
    purchase_date = models.DateField(null=True)
    order_number = models.IntegerField(null=True, default=0)
    purchase_cost = models.DecimalField(max_digits=64, decimal_places=2, null=True, default=0)
    warranty = models.IntegerField(null=True, default=0)
    notes = models.TextField(null=True)
    localiton = models.ForeignKey("Location", null=True)
    supplier = models.ForeignKey("Supplier", null=True)
    application = models.ForeignKey("Application", null=True)
    model = models.ForeignKey("Hardware", null=True)
    status = models.ForeignKey("Status", null=True)
    company = models.ForeignKey("Company", null=True)


class Status(models.Model):
    status = models.CharField(max_length=64, null=True)


class DashUser(models.Model):
    fullname = models.CharField(max_length=64, null=True)
