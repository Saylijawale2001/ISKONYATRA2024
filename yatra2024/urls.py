from django.urls import path

from . import views
from .views import *
from ISKON_yatra2024 import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', login, name='login'),

    path('customerhome/', customer_home_view, name='customerhome'),
    path('custregistration/', CustRegistrationView, name='CustRegistrationView'),

]
