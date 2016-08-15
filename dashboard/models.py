from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from web.models import Customer

CURRENCIES = (
    ("$", "$"),
)

COUNTRIES = (
    ("Turkey", "Turkey"),
)

CATEGORY_TYPES = (
    ("Asset", "Asset"),
    ("Access Point", "Access Point"),
    ("Chassis", "Chassis"),
    ("Computer", "Computer"),
    ("Switch", "Switch"),
    ("Router", "Router"),
    ("Firewall", "Firewall"),
    ("Printer", "Printer"),
    ("Scanner", "Scanner"),
    ("Projector", "Projector"),
    ("Phone", "Phone"),
    ("Tablet", "Tablet"),
    ("Mobile Phone", "Mobile Phone"),
    ("Video Conference", "Video Conference"),
    ("VoIP Gateway", "VoIP Gateway"),
    ("VoIP Phone", "VoIP Phone"),
    ("Monitor", "Monitor"),
    ("KVM (Keyboard, Video, Mouse switch)", "KVM (Keyboard, Video, Mouse switch)"),
    ("Load Balancer", "Load Balancer"),
    ("SAN (Storage Area Network)", "SAN (Storage Area Network)"),
    ("NAS (Network Attached Storage", "NAS (Network Attached Storage)"),
    ("Tape Library", "Tape Library"),
    ("UPS", "UPS"),
    ("General Purpose", "General Purpose"),
    ("Other Computer Device", "Other Computer Device"),
    ("Other Network Device", "Other Network Device"),
    ("Other Security Device", "Other Security Device"),
    ("Other Storage Device", "Other Storage Device"),
    ("Other Telecom Device", "Other Telecom Device"),
    ("Other Device", "Other Device"),
)

MEMORY_TYPES = (
    ("TB", "TB"),
    ("GB", "GB"),
    ("MB", "MB"),
)

PLATFORMS = (
    ("Physical", "Physical"),
)

STATUS = (
    ("Physical", "Physical"),
    ("Ready to Deploy", "Ready to Deploy"),
)


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, null=True)
    customer = models.ForeignKey(Customer, null=True)


class Company(models.Model):
    name = models.CharField(max_length=64, null=True)
    customer = models.ForeignKey(Customer, null=True)


class Location(models.Model):
    name = models.CharField(max_length=64, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    location_currency = models.CharField(null=True, max_length=64, choices=CURRENCIES)
    address = models.TextField(null=True)
    city = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=64, null=True)
    postal_code = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=64, null=True, choices=COUNTRIES)
    customer = models.ForeignKey(Customer, null=True)


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
    customer = models.ForeignKey(Customer, null=True)


class Software(models.Model):
    name = models.CharField(max_length=64, null=True)
    company = models.ForeignKey("Company", null=True)
    customer = models.ForeignKey(Customer, null=True)
    serial = models.CharField(max_length=64, null=True)
    licensed_to_name = models.CharField(max_length=64, null=True)
    licensed_to_email = models.EmailField(blank=True)
    seats = models.IntegerField(null=True, default=0)
    reassignable = models.BooleanField(default=False)
    maintained = models.BooleanField(default=False)
    supplier = models.ForeignKey("Supplier", null=True)
    purchase_date = models.DateField(null=True)
    order_number = models.IntegerField(null=True, default=0)
    purchase_cost = models.DecimalField(max_digits=64, decimal_places=2, null=True, default=0)
    expiration_date = models.DateField(null=True)
    termination_date = models.DateField(null=True)
    notes = models.TextField(null=True)


class Hardware(models.Model):
    manufacturer = models.ForeignKey("Manufacturer")
    category = models.CharField(max_length=64, null=True, choices=CATEGORY_TYPES)
    model = models.CharField(max_length=64, null=True)
    notes = models.TextField(null=True)
    image = models.ImageField(upload_to="suppliers")
    customer = models.ForeignKey(Customer, null=True)

    def __str__(self):
        return self.model


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
    os = models.CharField(max_length=64, null=True)
    platform = models.CharField(max_length=64, null=True, choices=PLATFORMS)
    serial = models.CharField(max_length=64, null=True)
    purchase_date = models.DateField(null=True)
    order_number = models.IntegerField(null=True, default=0)
    purchase_cost = models.DecimalField(max_digits=64, decimal_places=2, null=True, default=0)
    warranty = models.IntegerField(null=True, default=0)
    notes = models.TextField(null=True)
    location = models.ForeignKey("Location", null=True)
    supplier = models.ForeignKey("Supplier", null=True)
    application = models.ForeignKey("Software", null=True)
    model = models.ForeignKey("Hardware", null=True)
    status = models.CharField(max_length=64, null=True, choices=STATUS)
    company = models.ForeignKey("Company", null=True)
    customer = models.ForeignKey(Customer, null=True)


class DashUser(models.Model):
    fullname = models.CharField(max_length=64, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=64, null=True)
    postal_code = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=64, null=True, choices=COUNTRIES)
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    notes = models.TextField(null=True)
    customer = models.ForeignKey(Customer, null=True)
