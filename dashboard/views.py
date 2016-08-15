from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import View

from dashboard.forms import AssetForm
from dashboard.models import Hardware, Asset, Manufacturer, Supplier, Location, Software, DashUser, Company
from web.models import Customer, Account


class DashboardView(View):
    template_name = 'dashboard/index.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class AccountSettingsView(View):
    template_name = 'dashboard/account-settings.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class SubscriptionView(View):
    template_name = 'dashboard/subscription.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        plans = Account.objects.all().exclude(name=customer.plan_name, type=customer.type).exclude(type="Free")
        context = {"customer": customer, "plans":plans}
        return render(request, self.template_name, context)


class AssetsView(View):
    template_name = 'dashboard/assets.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        assets = Asset.objects.filter(customer=customer)
        context = {"customer": customer, "data": assets}
        return render(request, self.template_name,context)


class AssetShowView(View):
    template_name = 'dashboard/layouts/asset_show.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        assets = Asset.objects.filter(customer=customer)
        context = {"customer": customer, "data": assets}
        return render(request, self.template_name,context)


class AssetNewView(View):
    template_name = 'dashboard/layouts/asset_new.html'
    form_class = AssetForm

    @method_decorator(login_required)
    def get(self, request, *args):
        form = self.form_class
        if args:
            form = args[0]
        customer = Customer.objects.get(user=request.user)
        models = Hardware.objects.filter(customer=customer)
        context = {"customer": customer, "form": form, "models": models}

        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/assets')
        else:
            return self.get(request, form)



class BilingView(View):
    template_name = 'dashboard/biling.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        from paypal.standard.forms import PayPalPaymentsForm
        paypal_dict = {
            "business": "ci-facilitator@clouditam.com",
            "amount": "100.00",
            "item_name": "Pro Hesap",
            "invoice": "112931224",
            "notify_url": "http://127.0.0.1:8000" + reverse('paypal-ipn'),
            "return_url": "http://127.0.0.1:8000/paypal/",
            "cancel_return": "http://127.0.0.1:8000/paypal/",
            "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
        }

        # Create the instance.
        form = PayPalPaymentsForm(initial=paypal_dict)
        context = {"customer": customer,"form":form}
        return render(request, self.template_name,context)


class InvoicesView(View):
    template_name = 'dashboard/invoices.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class InvoiceDetailView(View):
    template_name = 'dashboard/layouts/invoice_base.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class ReportsView(View):
    template_name = 'dashboard/reports.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class SoftwareView(View):
    template_name = 'dashboard/software.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        software = Software.objects.filter(customer=customer)
        context = {"customer": customer, "data": software}
        return render(request, self.template_name, context)


class SoftwareShowView(View):
    template_name = 'dashboard/layouts/software_show.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        software = Software.objects.filter(customer=customer)
        context = {"customer": customer, "data": software}
        return render(request, self.template_name, context)


class SoftwareNewView(View):
    template_name = 'dashboard/layouts/software_new.html'
    form_class = AssetForm

    @method_decorator(login_required)
    def get(self, request, *args):
        form = self.form_class
        if args:
            form = args[0]
        customer = Customer.objects.get(user=request.user)
        models = Hardware.objects.filter(customer=customer)
        context = {"customer": customer, "form": form, "models": models}

        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/assets')
        else:
            return self.get(request, form)


class UsersView(View):
    template_name = 'dashboard/users.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        users = DashUser.objects.filter(customer=customer)
        context = {"customer": customer, "data": users}
        return render(request, self.template_name, context)


class UserShowView(View):
    template_name = 'dashboard/layouts/user_show.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        users = DashUser.objects.filter(customer=customer)
        context = {"customer": customer, "data": users}
        return render(request, self.template_name, context)


class UsersNewView(View):
    template_name = 'dashboard/layouts/user_new.html'
    form_class = AssetForm

    @method_decorator(login_required)
    def get(self, request, *args):
        form = self.form_class
        if args:
            form = args[0]
        customer = Customer.objects.get(user=request.user)
        models = Hardware.objects.filter(customer=customer)
        context = {"customer": customer, "form": form, "models": models}

        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/assets')
        else:
            return self.get(request, form)


class HardwareView(View):
    template_name = 'dashboard/hardware.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        hardware = Hardware.objects.filter(customer=customer)
        context = {"customer": customer, "data": hardware}
        return render(request, self.template_name, context)


class HardwareNewView(View):
    template_name = 'dashboard/layouts/hardware_new.html'
    form_class = AssetForm

    @method_decorator(login_required)
    def get(self, request, *args):
        form = self.form_class
        if args:
            form = args[0]
        customer = Customer.objects.get(user=request.user)
        models = Hardware.objects.filter(customer=customer)
        context = {"customer": customer, "form": form, "models": models}

        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/assets')
        else:
            return self.get(request, form)


class CompanyView(View):
    template_name = 'dashboard/company.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        companies = Company.objects.filter(customer=customer)
        context = {"customer": customer, "data": companies}
        return render(request, self.template_name, context)


class CompanyNewView(View):
    template_name = 'dashboard/layouts/company_new.html'
    form_class = AssetForm

    @method_decorator(login_required)
    def get(self, request, *args):
        form = self.form_class
        if args:
            form = args[0]
        customer = Customer.objects.get(user=request.user)
        models = Hardware.objects.filter(customer=customer)
        context = {"customer": customer, "form": form, "models": models}

        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/assets')
        else:
            return self.get(request, form)


class LocationView(View):
    template_name = 'dashboard/location.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        locations = Location.objects.filter(customer=customer)
        context = {"customer": customer, "data": locations}
        return render(request, self.template_name, context)


class LocationNewView(View):
    template_name = 'dashboard/layouts/location_new.html'
    form_class = AssetForm

    @method_decorator(login_required)
    def get(self, request, *args):
        form = self.form_class
        if args:
            form = args[0]
        customer = Customer.objects.get(user=request.user)
        locations = Location.objects.filter(customer=customer)
        context = {"customer": customer, "form": form, "locations": locations}

        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/assets')
        else:
            return self.get(request, form)


class ManufacturersView(View):
    template_name = 'dashboard/manufacturers.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        manufacturers = Manufacturer.objects.filter(customer=customer)
        context = {"customer": customer, "data": manufacturers}
        return render(request, self.template_name, context)


class ManufacturersNewView(View):
    template_name = 'dashboard/layouts/manufacturers_new.html'
    form_class = AssetForm

    @method_decorator(login_required)
    def get(self, request, *args):
        form = self.form_class
        if args:
            form = args[0]
        customer = Customer.objects.get(user=request.user)
        models = Hardware.objects.filter(customer=customer)
        context = {"customer": customer, "form": form, "models": models}

        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/assets')
        else:
            return self.get(request, form)


class SupplierView(View):
    template_name = 'dashboard/supplier.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        suppliers = Supplier.objects.filter(customer=customer)
        context = {"customer": customer, "data": suppliers}
        return render(request, self.template_name, context)


class SupplierNewView(View):
    template_name = 'dashboard/layouts/supplier_new.html'
    form_class = AssetForm

    @method_decorator(login_required)
    def get(self, request, *args):
        form = self.form_class
        if args:
            form = args[0]
        customer = Customer.objects.get(user=request.user)
        models = Hardware.objects.filter(customer=customer)
        context = {"customer": customer, "form": form, "models": models}

        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/assets')
        else:
            return self.get(request, form)