import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

CURRENCIES = (
    ("", "Select Curency"),
    ("$", "$"),
)

COUNTRIES = (
    ('', 'Select Country'),
    ("Turkey", "Turkey"),
)

CATEGORY_TYPES = (
    ("", "Select Category Type"),
    ("ASS", "Asset"),
    ("ACP", "Access Point"),
    ("CHS", "Chassis"),
    ("CMP", "Computer"),
    ("SWT", "Switch"),
    ("RTR", "Router"),
    ("FRW", "Firewall"),
    ("PRT", "Printer"),
    ("SCN", "Scanner"),
    ("PRJ", "Projector"),
    ("PHN", "Phone"),
    ("TBL", "Tablet"),
    ("MPH", "Mobile Phone"),
    ("VCF", "Video Conference"),
    ("VGW", "VoIP Gateway"),
    ("VPH", "VoIP Phone"),
    ("Monitor", "Monitor"),
    ("KVM", "KVM (Keyboard, Video, Mouse switch)"),
    ("BLC", "Load Balancer"),
    ("SAN", "SAN (Storage Area Network)"),
    ("NAS", "NAS (Network Attached Storage)"),
    ("TLB", "Tape Library"),
    ("UPS", "UPS"),
    ("GNR", "General Purpose"),
    ("OCP", "Other Computer Device"),
    ("ONP", "Other Network Device"),
    ("OSD", "Other Security Device"),
    ("OGD", "Other Storage Device"),
    ("OTD", "Other Telecom Device"),
    ("OTH", "Other Device"),
)

MEMORY_TYPES = (
    ("", "Select Type"),
    ("TB", "TB"),
    ("GB", "GB"),
    ("MB", "MB"),
)


class Company(models.Model):
    name = models.CharField(max_length=255, null=True)


class Location(models.Model):
    name = models.CharField(max_length=255, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    location_currency = models.CharField(null=True, max_length=255, choices=CURRENCIES, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, choices=COUNTRIES)


class Supplier(models.Model):
    name = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, choices=COUNTRIES, blank=True)
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    fax_number = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="suppliers", blank=True)


class Software(models.Model):
    name = models.CharField(max_length=255, null=True)
    company = models.ForeignKey("Company", null=True, blank=True)
    serial = models.CharField(max_length=255, null=True)
    licensed_to_name = models.CharField(max_length=255, null=True, blank=True)
    licensed_to_email = models.EmailField(blank=True, null=True)
    seats = models.IntegerField(null=True)
    reassignable = models.BooleanField(default=False, blank=True)
    maintained = models.BooleanField(default=False, blank=True)
    supplier = models.ForeignKey("Supplier", null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    order_number = models.IntegerField(null=True, blank=True)
    purchase_cost = models.DecimalField(max_digits=64, decimal_places=2, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    is_os = models.BooleanField(default=False, blank=True)
    assigned_to = models.ForeignKey("DashUser", null=True, blank=True)


class Hardware(models.Model):
    manufacturer = models.ForeignKey("Manufacturer", null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY_TYPES)
    model = models.CharField(max_length=255, null=True)
    notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="suppliers", blank=True)

    def __str__(self):
        return self.model


class Asset(models.Model):
    STATUS = (
        ("", "Select Status"),
        ("Ready to Deploy", "Ready to Deploy"),
        ("Unassign", "Unassign"),
    )
    PLATFORMS = (
        ("", "Select Platform"),
        ("Physical", "Physical"),
        ("Virtual", "Virtual"),
        ("Azure", "Azure"),
        ("Amazon Web Services", "Amazon Web Services"),
    )

    name = models.CharField(max_length=255, null=True, blank=True)
    asset_tag = models.CharField(max_length=12, editable=False, default="UNKNOWN")
    memory_size = models.DecimalField(max_digits=64, decimal_places=2, null=True, blank=True)
    memory_type = models.CharField(max_length=255, null=True, choices=MEMORY_TYPES, blank=True)
    cpu_speed = models.DecimalField(max_digits=64, decimal_places=2, null=True, blank=True)
    cpu_count = models.IntegerField(null=True, blank=True)
    disk_size = models.DecimalField(max_digits=64, decimal_places=2, null=True, blank=True)
    disk_type = models.CharField(max_length=255, null=True, choices=MEMORY_TYPES, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    os = models.ForeignKey("Software", null=True, blank=True, related_name="os")
    platform = models.CharField(max_length=255, null=True, choices=PLATFORMS, blank=True)
    serial = models.CharField(max_length=255, null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    order_number = models.IntegerField(null=True, blank=True)
    purchase_cost = models.DecimalField(max_digits=64, decimal_places=2, null=True, blank=True)
    warranty = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    location = models.ForeignKey("Location", null=True, blank=True)
    supplier = models.ForeignKey("Supplier", null=True, blank=True)
    application = models.ManyToManyField("Software", blank=True, related_name='software')
    model = models.ForeignKey("Hardware", null=True)
    status = models.CharField(max_length=255, null=True, choices=STATUS)
    company = models.ForeignKey("Company", null=True, blank=True)
    assigned_to = models.ForeignKey("DashUser", null=True, blank=True)


class DashUser(models.Model):
    fullname = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, choices=COUNTRIES, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    email = models.EmailField()
    notes = models.TextField(null=True, blank=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, null=True)
