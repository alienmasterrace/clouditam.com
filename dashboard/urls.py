from django.conf.urls import url
from dashboard.views import *

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name="dashboard"),
    url(r'^account-settings/$', AccountSettingsView.as_view(), name='account-settings'),
    url(r'^subscription/$', SubscriptionView.as_view(), name='subscription'),
    url(r'^biling/$', BilingView.as_view(), name='biling'),
    url(r'^invoices/$', InvoicesView.as_view(), name='invoices'),
    url(r'^assets/$', AssetsView.as_view(), name='assets'),
    url(r'^software/$', SoftwareView.as_view(), name='software'),
    url(r'^users/$', UsersView.as_view(), name='users'),
    url(r'^reports/$', ReportsView.as_view(), name='reports'),
]