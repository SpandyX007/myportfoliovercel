from django.db import models
# Create your models here.
class contactmemodel(models.Model):
    name_model=models.CharField(max_length=150,null=False, blank=False)
    email_model=models.EmailField(max_length=254,null=False, blank=False)
    contactnumber_model=models.CharField(max_length=12,null=False, blank=False)
    designation_model=models.CharField(max_length=100,null=False, blank=False)
    subject_model=models.CharField(max_length=150,null=False, blank=False)
    message_model=models.CharField(max_length=500,null=False, blank=False)

class projectsmodel(models.Model):
    projectname=models.CharField(max_length=100, null=False, blank=False)
    projectimg=models.ImageField(upload_to='projectsimg/')
    projectdesc=models.CharField(max_length=500)
    projectcategory=models.CharField(max_length=50)
    projectdate=models.CharField(max_length=11)
    projecturl=models.CharField(max_length=1000000,default="1234")
    projectgithuburl=models.CharField(max_length=1000000,default="1234")

class reviewmodel(models.Model):
    reviewdesc=models.CharField(max_length=300)
    reviewimg=models.FileField(upload_to='reviewimg/')
    reviewname=models.CharField(max_length=20)
    reviewprofession=models.CharField(max_length=50)