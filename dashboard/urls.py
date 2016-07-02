from django.conf.urls import url
from dashboard.views import *

urlpatterns = [
    url(r'^$', DashboardView.as_view()),
]