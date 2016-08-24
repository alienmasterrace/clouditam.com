from django.contrib import admin
from web.models import Header, Customer, Account, Setting, Feature, Demo, Client, About, Contact

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True

    def has_delete_permission(self, request, obj=None):
        return False if self.model.objects.count() <= 1 else True

    def get_actions(self, request):
        actions = super(HeaderAdmin,self).get_actions(request)
        if (self.model.objects.count() <= 1):
            del actions['delete_selected']
        return actions

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True

    def has_delete_permission(self, request, obj=None):
        return False if self.model.objects.count() <= 1 else True

    def get_actions(self, request):
        actions = super(AboutAdmin, self).get_actions(request)
        if (self.model.objects.count() <= 1):
            del actions['delete_selected']
        return actions

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True

    def has_delete_permission(self, request, obj=None):
        return False if self.model.objects.count() <= 1 else True

    def get_actions(self, request):
        actions = super(ContactAdmin, self).get_actions(request)
        if (self.model.objects.count() <= 1):
            del actions['delete_selected']
        return actions



@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True

    def has_delete_permission(self, request, obj=None):
        return False if self.model.objects.count() <= 1 else True

    def get_actions(self, request):
        actions = super(SettingsAdmin, self).get_actions(request)
        if (self.model.objects.count() <= 1):
            del actions['delete_selected']
        return actions

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title','text')

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 5 else True

@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ('title','text')

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 2 else True