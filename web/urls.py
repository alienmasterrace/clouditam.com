from django.conf.urls import url
from web.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^signin/$', SignInView.as_view(), name='signin'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]