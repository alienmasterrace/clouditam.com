from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View

from dashboard.forms import AssetForm, CompanyForm, ManufacturerForm, SupplierForm, SoftwareForm, DashUserForm, \
    HardwareForm, LocationForm
from dashboard.models import CATEGORY_TYPES, Asset, Software, DashUser
from web.models import Customer, Account
from django.contrib import messages
from django.contrib.admin.models import LogEntry, ADDITION


class DashboardView(View):
    template_name = 'dashboard/index.html'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)


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
        context = {"customer": customer, "plans": plans}
        return render(request, self.template_name, context)


class AssetsView(View):
    template_name = 'dashboard/assets.html'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)


class AssetShowView(View):
    template_name = 'dashboard/layouts/asset_show.html'

    @method_decorator(login_required)
    def get(self, request, tag):
        customer = Customer.objects.get(user=request.user)
        obj = get_object_or_404(Asset, asset_tag=tag, customer=customer)
        # logs = LogEntry.objects.filter(object_id=obj.id, content_type__id__exact=ContentType.objects.get_for_model(Asset).id)
        logs = obj.history.all().order_by('-timestamp')
        context = {"asset": obj, "history": logs}
        return render(request, self.template_name, context)


class AssetNewView(View):
    template_name = 'dashboard/layouts/asset_new.html'
    form_class = AssetForm

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(customer=customer)
        context = {"customer": customer, "form": form}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(request.POST, customer=customer)
        if form.is_valid():
            obj = form.save()
            cats = dict(CATEGORY_TYPES)
            obj.asset_tag = "{0}{1:04d}{2:05d}".format({cats[k]: k for k in cats}[obj.model.get_category_display()],
                                                       customer.id, obj.id)
            obj.save()
            customer.assets.add(obj)
            message = 'Asset "{0}" successfully added.'.format(form.cleaned_data['model'])
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('assets')
        else:
            print(form.errors)
            message = 'Something happened please try again.'
            messages.add_message(request, messages.ERROR, message)
            return self.get(request)


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
        context = {"customer": customer, "form": form}
        return render(request, self.template_name, context)


class InvoicesView(View):
    template_name = 'dashboard/invoices.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer}
        return render(request, self.template_name, context)


class InvoiceDetailView(View):
    template_name = 'dashboard/layouts/invoice_base.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer}
        return render(request, self.template_name, context)


class ReportsView(View):
    template_name = 'dashboard/reports.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer}
        return render(request, self.template_name, context)


class SoftwareView(View):
    template_name = 'dashboard/software.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        software = customer.softwares.all()
        context = {"customer": customer, "data": software}
        return render(request, self.template_name, context)


class SoftwareShowView(View):
    template_name = 'dashboard/layouts/software_show.html'

    @method_decorator(login_required)
    def get(self, request, id_obj):
        obj = get_object_or_404(Software, id=id_obj, customer=request.user.customer)
        logs = obj.history.all().order_by('-timestamp')
        seats = []
        s_number = 0
        if obj.seats:
            s_number = obj.seats
        for j in obj.software.all():
            d = {}
            d['asset'] = j
            d['user'] = j.assigned_to
            d['button'] = 'Unassign'
            seats.append(d)
        for i in range(s_number - len(seats)):
            n_d = {}
            n_d['button'] = 'Assign To'
            seats.append(n_d)
        context = {'software': obj, 'history': logs, 'seats': seats}
        return render(request, self.template_name, context)


class SoftwareNewView(View):
    template_name = 'dashboard/layouts/software_new.html'
    form_class = SoftwareForm

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(customer=customer)
        context = {"customer": customer, "form": form}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(request.POST, customer=customer)
        if form.is_valid():
            obj = form.save()
            customer.softwares.add(obj)
            message = 'Software "{0}" successfully added.'.format(form.cleaned_data['name'])
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('software')
        else:
            message = 'Something happened please try again.'
            messages.add_message(request, messages.ERROR, message)
            return self.get(request)


class UsersView(View):
    template_name = 'dashboard/users.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        users = customer.dashusers.all()
        context = {"customer": customer, "data": users}
        return render(request, self.template_name, context)


class UserShowView(View):
    template_name = 'dashboard/layouts/user_show.html'

    @method_decorator(login_required)
    def get(self, request, id_obj):
        obj = get_object_or_404(DashUser, id=id_obj, customer=request.user.customer)
        assigned_assets = obj.asset_set.all()
        assigned_softwares = obj.software_set.all()
        context = {"user": obj, 'assigned_assets': assigned_assets, 'assigned_softwares': assigned_softwares}
        return render(request, self.template_name, context)


class UsersNewView(View):
    template_name = 'dashboard/layouts/user_new.html'
    form_class = DashUserForm

    @method_decorator(login_required)
    def get(self, request):
        form = self.form_class()
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer, "form": form}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            Customer.objects.get(user=request.user).dashusers.add(obj)
            message = 'User "{0}" successfully added.'.format(form.cleaned_data['fullname'])
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('users')
        else:
            message = 'Something happened please try again.'
            messages.add_message(request, messages.ERROR, message)
            return self.get(request)


class HardwareView(View):
    template_name = 'dashboard/hardware.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        hardware = customer.hardwares.all()
        context = {"customer": customer, "data": hardware}
        return render(request, self.template_name, context)


class HardwareNewView(View):
    template_name = 'dashboard/layouts/hardware_new.html'
    form_class = HardwareForm

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(customer=customer)
        context = {"customer": customer, "form": form}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(request.POST, customer=customer)
        if form.is_valid():
            obj = form.save()
            customer.hardwares.add(obj)
            message = 'Hardware "{0}" successfully added.'.format(form.cleaned_data['model'])
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('hardware')
        else:
            message = 'Something happened please try again.'
            messages.add_message(request, messages.ERROR, message)
            return self.get(request)


class CompanyView(View):
    template_name = 'dashboard/company.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        companies = customer.companies.all()
        context = {"customer": customer, "data": companies}
        return render(request, self.template_name, context)


class CompanyNewView(View):
    template_name = 'dashboard/layouts/company_new.html'
    form_class = CompanyForm

    @method_decorator(login_required)
    def get(self, request):
        form = self.form_class()
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer, "form": form}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            customer.companies.add(obj)
            message = 'Company "{0}" successfully added.'.format(form.cleaned_data['name'])
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('company')
        else:
            message = 'Something happened please try again.'
            messages.add_message(request, messages.ERROR, message)
            return self.get(request)


class LocationView(View):
    template_name = 'dashboard/location.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        locations = customer.locations.all()
        context = {"customer": customer, "data": locations}
        return render(request, self.template_name, context)


class LocationNewView(View):
    template_name = 'dashboard/layouts/location_new.html'
    form_class = LocationForm

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(customer=customer)
        context = {"customer": customer, "form": form}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(request.POST, customer=customer)
        if form.is_valid():
            obj = form.save()
            customer.locations.add(obj)
            message = 'Location "{0}" successfully added.'.format(form.cleaned_data['name'])
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('location')
        else:
            message = '{0}'.format(form.errors)
            messages.add_message(request, messages.ERROR, message)
            return self.get(request)


class ManufacturersView(View):
    template_name = 'dashboard/manufacturers.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        manufacturers = customer.manufacturers.all()
        context = {"customer": customer, "data": manufacturers}
        return render(request, self.template_name, context)


class ManufacturersNewView(View):
    template_name = 'dashboard/layouts/manufacturers_new.html'
    form_class = ManufacturerForm

    @method_decorator(login_required)
    def get(self, request):
        form = self.form_class()
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer, "form": form}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            Customer.objects.get(user=request.user).manufacturers.add(obj)
            message = 'Manufacturer "{0}" successfully added.'.format(form.cleaned_data['name'])
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('manufacturers')
        else:
            message = 'Something happened please try again.'
            messages.add_message(request, messages.ERROR, message)
            return self.get(request)


class SupplierView(View):
    template_name = 'dashboard/supplier.html'

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        suppliers = customer.suppliers.all()
        context = {"customer": customer, "data": suppliers}
        return render(request, self.template_name, context)


class SupplierNewView(View):
    template_name = 'dashboard/layouts/supplier_new.html'
    form_class = SupplierForm

    @method_decorator(login_required)
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class()
        context = {"customer": customer, "form": form}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            customer.suppliers.add(obj)
            message = 'Supplier "{0}" successfully added.'.format(form.cleaned_data['name'])
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('supplier')
        else:
            message = 'Something happened please try again.'
            messages.add_message(request, messages.ERROR, message)
            return self.get(request)
