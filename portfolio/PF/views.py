from django.shortcuts import render
from .models import certificate,Project,feedback
# Create your views here.

from django.shortcuts import HttpResponse

def profile(request):
    # return HttpResponse("Hello World")
    
    return render(request,'home.html')

def ps(request):
    return render(request,'ps.html')

def skill(request):
    
    return render(request,'home.html')


def cert(request):
    cert = certificate.objects.all()
    return render(request, 'certificates.html', {'cert': cert})

def hireme(request):
    return render(request,'hireme.html')

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})


def feedback(request):
    return render(request,'feedback.html')