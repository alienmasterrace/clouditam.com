from django.contrib import admin

# Register your models here.
from dashboard.models import *


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    pass

@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    pass

@admin.register(DashUser)
class DashUserAdmin(admin.ModelAdmin):
    pass





