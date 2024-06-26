from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from.views import *

app_name = 'accounts'

urlpatterns = [
  path("login/", LoginView.as_view(template_name='accounts/login.html'), name='login'),
  path("logout/", LogoutView.as_view(), name="logout"),
  path("signup/", SignUp.as_view(), name='signup'),
]
