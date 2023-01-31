from django.shortcuts import render
from .models import certificate,Project,feedback
from django.contrib import messages
# Create your views here.

from django.shortcuts import HttpResponse

def profile(request):
    # return HttpResponse("Hello World")
    
    return render(request,'home.html')

def ps(request):
    return render(request,'ps.html')

def feedbacks(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email= request.POST['email']
        phone = request.POST['phone']
        mess= request.POST['feedback_text']
        feedback(name=fname,email=email,phone=phone,feedback_text=mess).save()
        messages.success(request,'FeedBack Submited Successfully')
        return render(request,'feedback.html')
    elif request.method=='GET':
        return render(request,'feedback.html')
    else:
        # return HttpResponse("An error Occured! Employee Has Not Been added")
    
        return render(request,'feedback.html') 
    
    return render(request,'feedback.html')


def cert(request):
    cert = certificate.objects.all()
    return render(request, 'certificates.html', {'cert': cert})

def hireme(request):
    
    
    return render(request,'hireme.html') 
    
    
    
    
def hireme2(request):
    return render(request,'hireme2.html')    
    

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})
