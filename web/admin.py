from django.contrib import admin
from web.models import Header, Customer, Account, Settings
# Register your models here.

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass