from django import forms

from dashboard.models import Asset, Hardware, Company, Manufacturer, Supplier, Software, DashUser, Location


class AssetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super(AssetForm, self).__init__(*args, **kwargs)

        if customer:
            self.fields['model'].queryset = Hardware.objects.filter(customer=customer)
            self.fields['location'].queryset = Location.objects.filter(customer=customer)
            self.fields['supplier'].queryset = Supplier.objects.filter(customer=customer)
            self.fields['company'].queryset = Company.objects.filter(customer=customer)
            self.fields['assigned_to'].queryset = DashUser.objects.filter(customer=customer)
            self.fields['os'].queryset = Software.objects.filter(customer=customer, is_os=True)

    class Meta:
        model = Asset
        exclude = ['application', 'asset_id', 'asset_tag']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = []


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        exclude = []


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = []


class SoftwareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super(SoftwareForm, self).__init__(*args, **kwargs)

        if customer:
            self.fields['supplier'].queryset = Supplier.objects.filter(customer=customer)
            self.fields['company'].queryset = Company.objects.filter(customer=customer)
            self.fields['assigned_to'].queryset = DashUser.objects.filter(customer=customer)

    class Meta:
        model = Software
        exclude = []


class DashUserForm(forms.ModelForm):
    class Meta:
        model = DashUser
        exclude = []


class HardwareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super(HardwareForm, self).__init__(*args, **kwargs)

        if customer:
            self.fields['manufacturer'].queryset = Manufacturer.objects.filter(customer=customer)

    class Meta:
        model = Hardware
        exclude = []


class LocationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super(LocationForm, self).__init__(*args, **kwargs)

        if customer:
            self.fields['parent'].queryset = Location.objects.filter(customer=customer)

    class Meta:
        model = Location
        exclude = []
