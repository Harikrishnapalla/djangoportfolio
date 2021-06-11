from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
# Create your views here.

def home(request):
    return render(request, 'html/index.html')

def error_404(request, exception):
    print("sdfddddfssfsf")
    data = {}
    return render(request,'html/404.html', data)

# def error_500(request,  exception):
#         data = {}
#         return render(request,'certman/500.html', data)