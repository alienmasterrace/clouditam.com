from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator


class IndexView(View):
    template_name = 'web/index.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class DashboardView(View):
    template_name = 'web/dashboard.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AccountView(View):
    template_name = 'web/account/profile.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class LoginView(View):
    template_name = 'web/index.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterView(View):
    template_name = 'web/index.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
