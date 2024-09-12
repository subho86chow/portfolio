from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from premailer import transform


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
    project = Projects.objects.filter(project_name = str).first()
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
            try:
                name = request.POST['name']
                cemail = request.POST['cemail']
                message = request.POST['message']
                Contact_message.objects.create(name = name, email=cemail,message=message)
                subject = 'Request Received – Thank You'
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [cemail]
                html_content = render_to_string('thank_you_mail.html', {'username':name})
                transformed_email = transform(html_content)
                email = EmailMultiAlternatives(subject, 'This is a plain text message.', from_email, to_email)
                email.attach_alternative(transformed_email, "text/html")
                email.send()
                return redirect('contact')
            except Exception as e:
                print(e)
                return redirect('contact')
        
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
    social_ins = social_links.objects.all().first()
    facebook = social_ins.facebook
    return redirect(facebook)

def instagram(request):
    social_ins = social_links.objects.all().first()
    instagram = social_ins.instagram
    return redirect(instagram)

def linkedin(request):
    social_ins = social_links.objects.all().first()
    linkedin = social_ins.linkedin
    return redirect(linkedin)

def calendely(request):
    social_ins = social_links.objects.all().first()
    calendely = social_ins.calendely
    return redirect(calendely)

def handeling404(request, exception):
    return render(request,'404.html',{})

