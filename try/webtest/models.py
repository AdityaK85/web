from operator import mod
from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from traitlets import default


# Create your models here.
class testmod(models.Model):
    name = models.CharField(max_length=2000)
    subject = models.CharField(max_length=2000)
    course = models.CharField(max_length=2000)
    year = models.IntegerField()
    
    
    def __str__(self): 
        return self.subject
    
        
class news(models.Model):
    title = models.CharField(max_length=200)
    news_desc = HTMLField()
    upl_img = models.FileField(upload_to = "jpeg/", max_length=100, null = True, default= None)
    new_slug = AutoSlugField(populate_from ='title', unique=True,null=True,default=None)
    
    def __str__(self):
        return self.title
    
    
class login(models.Model):
    username = models.CharField(max_length=80)
    email    = models.EmailField()
    profile_pic = models.ImageField( upload_to="media",blank = True)
    
    def __str__(self):
        return self.username
    
    
    


PESONALITY = (
    ('','Select The Personality'),
    ('Good Person','Good Person'),
    ('Inocent','Inocent'),
    ('Extrovert','Extrovert'),
)

SMOKER = (
    ('1','YES'),
    ('2','NO'),
)

class dropdown(models.Model):
    personality = models.CharField(max_length=100, null=True ,choices=PESONALITY)
    salary = models.CharField(max_length=100)
    gender =models.CharField(max_length=50)
    payment =models.CharField(max_length=50,null=True,blank=True)
    experience = models.BooleanField(null=True, default='none')
    smoker = models.CharField(max_length=100, null=True ,choices=SMOKER, default='')


class select_muliple(models.Model):
    option = models.CharField(max_length=50,null=True,blank=True)


class advancedAjax(models.Model):
    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=50,null=True,blank=True)
    profile_img = models.FileField(upload_to="ProfileImage", blank=True, null=True)