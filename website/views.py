from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        Customer_emails.objects.create(email=email)
        return redirect('calendely')
    return render(request,"home.html")

def portfolio(request):
    projects = Projects.objects.all()
    context = {'projects':projects}
    return render(request,"portfolio.html",context)

def project_details(request,str):
    project = Projects.objects.filter(project_name = str)
    context = {'project':project,'navbar':"portfolio"}
    return render(request,"project_details.html",context)

def services(request):
    if request.method == 'POST':
        email = request.POST['email']
        Customer_emails.objects.create(email=email)
        return redirect('contact')
    testimonials = Testimonials.objects.all()
    technologies = Technology.objects.all()
    context = {'testimonials':testimonials,'technologies':technologies, 'navbar':"services"}

    return render(request,"services.html",context)

def contact(request):
    if request.method == 'POST':
        if 'email_submit' in request.POST:
            email = request.POST['email']
            Customer_emails.objects.create(email=email)
            return redirect('contact')
        
        if 'message_submit' in request.POST:
            name = request.POST['name']
            cemail = request.POST['cemail']
            message = request.POST['message']
            Contact_message.objects.create(name = name, email=cemail,message=message)
            return redirect('home')
    context = {'navbar':"contact"}
    return render(request,"contact.html",context)

def webdev(request):
    context = {'navbar':"services"}
    return render(request,'webdev.html',context)

def marketing(request):
    context = {'navbar':"services"}
    return render(request,'marketing.html',context)

def designing(request):
    context = {'navbar':"services"}
    return render(request,'brand_design.html',context)

def customdev(request):
    context = {'navbar':"services"}
    return render(request,'customdev.html',context)

def facebook(request):
    facebook = 'https://www.facebook.com/profile.php?id=100083938923609'
    return redirect(facebook)

def instagram(request):
    instagram = 'https://www.instagram.com/shubhajit_ch0wdhury/'
    return redirect(instagram)

def linkedin(request):
    linkedin = 'https://www.linkedin.com/in/shubhajit--chowdhury/'
    return redirect(linkedin)

def calendely(request):
    calendely = 'https://calendly.com/itsmeshubho/schedule-a-virtual-meeting'
    return redirect(calendely)