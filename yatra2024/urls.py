from django.urls import path

from . import views
from .views import *
from ISKON_yatra2024 import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('custregistration/', views.CustRegistrationView, name='custregistration'),

]
