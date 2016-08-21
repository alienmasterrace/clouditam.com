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
    list_display = ('maintenance_message', 'maintenance_mode')

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True

    def has_delete_permission(self, request, obj=None):
        return False if self.model.objects.count() <= 1 else True

    def get_actions(self, request):
        actions = super(SettingsAdmin, self).get_actions(request)
        if (self.model.objects.count() <= 1):
            del actions['delete_selected']
        return actions