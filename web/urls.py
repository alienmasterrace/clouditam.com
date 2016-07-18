from django.conf.urls import url
from web.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^pricing/$', PricingView.as_view(), name='pricing'),
    url(r'^clients/$', ClientsView.as_view(), name='clients'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^signin/$', SignInView.as_view(), name='signin'),
    url(r'^account/$', AccountView.as_view(), name='account'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]