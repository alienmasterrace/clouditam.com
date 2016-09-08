from django.conf.urls import url
from dashboard.views import *

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name="dashboard"),
    url(r'^account-settings/$', AccountSettingsView.as_view(), name='account-settings'),
    url(r'^subscription/$', SubscriptionView.as_view(), name='subscription'),
    # url(r'^biling/$', BilingView.as_view(), name='biling'),
    url(r'^invoices/$', InvoicesView.as_view(), name='invoices'),
    url(r'^invoices/show$', InvoiceDetailView.as_view(), name='invoice_detail'),
    url(r'^assets/$', AssetsView.as_view(), name='assets'),
    url(r'^assets/new$', AssetNewView.as_view(), name='asset_new'),
    url(r'^assets/edit/(?P<id_obj>[\w-]+)/$', AssetEditView.as_view(), name='asset_edit'),
    url(r'^assets/duplicate/(?P<id_obj>[\w-]+)/$', AssetDuplicateView.as_view(), name='asset_duplicate'),
    url(r'^assets/delete/(?P<id_obj>[\w-]+)/$', AssetDeleteView.as_view(), name='asset_delete'),
    url(r'^assets/show/(?P<tag>[\w-]+)/$', AssetShowView.as_view(), name='asset_show'),
    url(r'^software/$', SoftwareView.as_view(), name='software'),
    url(r'^software/new$', SoftwareNewView.as_view(), name='software_new'),
    url(r'^software/edit/(?P<id_obj>[\w-]+)/$', SoftwareEditView.as_view(), name='software_edit'),
    url(r'^software/duplicate/(?P<id_obj>[\w-]+)/$', SoftwareDuplicateView.as_view(), name='software_duplicate'),
    url(r'^software/delete/(?P<id_obj>[\w-]+)/$', SoftwareDeleteView.as_view(), name='software_delete'),
    url(r'^software/show/(?P<id_obj>[\w-]+)/$', SoftwareShowView.as_view(), name='software_show'),
    url(r'^users/$', UsersView.as_view(), name='users'),
    url(r'^users/new$', UsersNewView.as_view(), name='users_new'),
    url(r'^users/show/(?P<id_obj>[\w-]+)/$', UserShowView.as_view(), name='user_show'),
    url(r'^users/edit/(?P<id_obj>[\w-]+)/$', UserEditView.as_view(), name='user_edit'),
    url(r'^users/duplicate/(?P<id_obj>[\w-]+)/$', UserDuplicateView.as_view(), name='user_duplicate'),
    url(r'^users/delete/(?P<id_obj>[\w-]+)/$', UserDeleteView.as_view(), name='user_delete'),
    # url(r'^reports/$', ReportsView.as_view(), name='reports'),
    url(r'^company/$', CompanyView.as_view(), name='company'),
    url(r'^company/new$', CompanyNewView.as_view(), name='company_new'),
    url(r'^company/edit/(?P<id_obj>[\w-]+)/$', CompanyEditView.as_view(), name='company_edit'),
    url(r'^company/duplicate/(?P<id_obj>[\w-]+)/$', CompanyDuplicateView.as_view(), name='company_duplicate'),
    url(r'^company/delete/(?P<id_obj>[\w-]+)/$', CompanyDeleteView.as_view(), name='company_delete'),
    url(r'^hardware/$', HardwareView.as_view(), name='hardware'),
    url(r'^hardware/new$', HardwareNewView.as_view(), name='hardware_new'),
    url(r'^hardware/edit/(?P<id_obj>[\w-]+)/$', HardwareEditView.as_view(), name='hardware_edit'),
    url(r'^hardware/duplicate/(?P<id_obj>[\w-]+)/$', HardwareDuplicateView.as_view(), name='hardware_duplicate'),
    url(r'^hardware/delete/(?P<id_obj>[\w-]+)/$', HardwareDeleteView.as_view(), name='hardware_delete'),
    url(r'^location/$', LocationView.as_view(), name='location'),
    url(r'^location/new$', LocationNewView.as_view(), name='location_new'),
    url(r'^location/edit/(?P<id_obj>[\w-]+)/$', LocationEditView.as_view(), name='location_edit'),
    url(r'^location/duplicate/(?P<id_obj>[\w-]+)/$', LocationDuplicateView.as_view(), name='location_duplicate'),
    url(r'^location/delete/(?P<id_obj>[\w-]+)/$', LocationDeleteView.as_view(), name='location_delete'),
    url(r'^manufacturers/$', ManufacturersView.as_view(), name='manufacturers'),
    url(r'^manufacturers/new$', ManufacturersNewView.as_view(), name='manufacturers_new'),
    url(r'^manufacturers/edit/(?P<id_obj>[\w-]+)/$', ManufacturersEditView.as_view(), name='manufacturers_edit'),
    url(r'^manufacturers/duplicate/(?P<id_obj>[\w-]+)/$', ManufacturersDuplicateView.as_view(), name='manufacturers_duplicate'),
    url(r'^manufacturers/delete/(?P<id_obj>[\w-]+)/$', ManufacturersDeleteView.as_view(), name='manufacturers_delete'),
    url(r'^supplier/$', SupplierView.as_view(), name='supplier'),
    url(r'^supplier/new$', SupplierNewView.as_view(), name='supplier_new'),
    url(r'^supplier/edit/(?P<id_obj>[\w-]+)/$', SupplierEditView.as_view(), name='supplier_edit'),
    url(r'^supplier/duplicate/(?P<id_obj>[\w-]+)/$', SupplierDuplicateView.as_view(), name='supplier_duplicate'),
    url(r'^supplier/delete/(?P<id_obj>[\w-]+)/$', SupplierDeleteView.as_view(), name='supplier_delete'),
]
