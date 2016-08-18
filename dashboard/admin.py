from django.contrib import admin

# Register your models here.
from dashboard.models import *
from web.models import Customer


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    readonly_fields = ('asset_tag','id')

    def save_model(self, request, obj, form, change):
        obj.save()
        customer = Customer.objects.get(user=request.user)
        cats = dict(CATEGORY_TYPES)
        obj.asset_tag = "{0}{1:04d}{2:05d}".format({cats[k]: k for k in cats}[obj.model.get_category_display()],
                                                   customer.id, obj.id)
        obj.save()
        customer.assets.add(obj)

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





