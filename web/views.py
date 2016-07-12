from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.utils.datetime_safe import datetime
from django.views.generic import View
from django.utils.decorators import method_decorator
from web.forms import SignUpForm, SignInForm


class IndexView(View):
    template_name = 'web/index.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class PricingView(View):
    template_name = 'web/pricing.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AccountView(View):
    template_name = 'web/account/profile.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SignInView(View):
    template_name = 'web/signin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['username_or_email'], password=form.data['passwrd'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    error_msg = 'There was an error!'
                    return render(request, self.template_name, {'form': form, 'error_msg': error_msg})
            else:
                error_msg = 'There was an error!'
                return render(request, self.template_name, {'form': form, 'error_msg': error_msg})
        else:
            error_msg = 'There was an error!'
            return render(request, self.template_name, {'form': form, 'error_msg': error_msg})


class SignUpView(View):
    template_name = 'web/index.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        print(form.errors)
        return HttpResponseRedirect('/')


class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')
