
from django import forms
from django.contrib import admin
from django.forms import ModelForm
from  webtest.models import *
from django.forms import ModelForm
# Register your models here.

class login_password(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class meta():
        model = login
        fields = ('__all__')

admin.site.register(testmod)
admin.site.register(news)
admin.site.register(login)
admin.site.register(dropdown)
admin.site.register(select_muliple)
admin.site.register(advancedAjax)
