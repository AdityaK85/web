from django import forms

class inputform(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()    


from .models import *
 
# create a ModelForm
class selections(forms.ModelForm):
    GENDER = [
        ('Male','male'),
        ('Female','female'),
        ('Other','Other'),
        ]
    
    PAYMENT = [
        ('Internet','Internet'),
        ('Cash','Cash'),
        ('Online','Online'),
        ('Credit','Credit'),
    ]
    
    gender = forms.CharField(label='Gender',  widget=forms.RadioSelect(choices=GENDER))
    payment = forms.CharField(label='Gender',  widget=forms.CheckboxSelectMultiple(choices=PAYMENT))
    class Meta:  
        
        model = dropdown
        exclude = ['created_at', 'Situation']
        