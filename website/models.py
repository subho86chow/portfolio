from django.db import models

# Create your models here.

class Projects(models.Model):
    project_name = models.CharField(max_length = 50,blank=True,null=True)
    project_type = models.CharField(max_length = 50,blank=True,null=True)
    client_name = models.CharField(max_length = 50,blank=True,null=True)
    project_date = models.CharField(max_length = 50,blank=True,null=True)
    main_text = models.TextField(max_length = 100,blank=True,null=True)
    sub_text1 = models.TextField(max_length = 500,blank=True,null=True)
    sub_text2 = models.TextField(max_length = 500,blank=True,null=True)
    labelimg = models.ImageField(upload_to='images/uploads/',null=True,blank=True)
    subimg1 = models.ImageField(upload_to='images/uploads/',null=True,blank=True)
    subimg2 = models.ImageField(upload_to='images/uploads/',null=True,blank=True)
    subimg3 = models.ImageField(upload_to='images/uploads/',null=True,blank=True)
    subimg4 = models.ImageField(upload_to='images/uploads/',null=True,blank=True)
    endimg1 = models.ImageField(upload_to='images/uploads/',null=True,blank=True)
    endimg2 = models.ImageField(upload_to='images/uploads/',null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.project_name)
    
    def get_absolute_url(self):
        return f'/portfolio/{self.project_name}/'
    
    

class Testimonials(models.Model):
    project_name = models.OneToOneField(Projects,on_delete = models.CASCADE)
    client_name = models.CharField(max_length = 50,blank=True,null=True)
    client_photo = models.ImageField(upload_to='images/uploads/',null=True,blank=True)
    project_review = models.CharField(max_length =200, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.project_name)
    
class Technology(models.Model):
    technology_name = models.CharField(max_length = 20,null=True,blank = True)
    technology_photo = models.ImageField(upload_to='images/uploads/',null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.technology_name)
    

class Customer_emails(models.Model):
    email = models.CharField(max_length=80,null=True,blank=True)
    date_created = models.DateField(auto_now_add = True)

    def __str__(self):
        return str(self.email)
    

class Contact_message(models.Model):
    name= models.CharField(max_length= 50,null= True, blank = True)
    email= models.CharField(max_length= 100,null= True, blank = True)
    message= models.CharField(max_length= 500,null= True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)
    

class social_links(models.Model):
    facebook = models.CharField(max_length=200,blank=True, null=True)
    instagram = models.CharField(max_length=200,blank=True, null=True)
    linkedin = models.CharField(max_length=200,blank=True, null=True)
    calendely = models.CharField(max_length=200,blank=True, null=True)
    
    def __str__(self):
        return "Social Links"
