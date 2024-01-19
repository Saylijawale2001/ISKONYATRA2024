from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import request

from ISKON_yatra2024 import settings
from django.shortcuts import render, redirect, HttpResponse

def login(request):
    return render(request, 'login.html')

def customerhome(request):
    return render(request, 'customerhome.html')

def CustRegistrationView(request):
    return render(request, 'custregistration.html')