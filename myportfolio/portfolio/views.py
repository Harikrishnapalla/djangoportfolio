from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
# Create your views here.

def home(request):
    return render(request, 'html/index.html')