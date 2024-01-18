from django.urls import path
from .views import home
from ISKON_yatra2024 import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
]
