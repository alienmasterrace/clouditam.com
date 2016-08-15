from django import forms

from dashboard.models import Asset, Hardware


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        exclude = []


