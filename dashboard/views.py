from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import View

from web.models import Customer, Account


class DashboardView(View):
    template_name = 'dashboard/index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class AccountSettingsView(View):
    template_name = 'dashboard/account-settings.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class SubscriptionView(View):
    template_name = 'dashboard/subscription.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        plans = Account.objects.all().exclude(name=customer.plan_name, type=customer.type).exclude(type="Free")
        context = {"customer": customer, "plans":plans}
        return render(request, self.template_name, context)


class AssetsView(View):
    template_name = 'dashboard/assets.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name,context)


class BilingView(View):
    template_name = 'dashboard/biling.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name,context)


class InvoicesView(View):
    template_name = 'dashboard/invoices.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class ReportsView(View):
    template_name = 'dashboard/reports.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class SoftwareView(View):
    template_name = 'dashboard/software.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)


class UsersView(View):
    template_name = 'dashboard/users.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        context = {"customer": customer,}
        return render(request, self.template_name, context)
