from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

s=[('a','A'),('b','B'),('c','C')]
b= [('Computer science','CSE'),('Information Technology','IT'),('Electronics And Communications','ECE'),('Mechanical','Mech'),('EEE','EEE'),('Civil','Civil')]

class StudentForm(ModelForm):
    section = forms.CharField(
        label='Section',
        widget=forms.Select(choices=s),
    )
    branch=forms.CharField(label='Branch', widget=forms.Select(choices=b))
    class Meta:
        model=Student
        fields='__all__'
        exclude=['user','name']


"""class StudentPostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','desc']"""
class StudentPostForm(ModelForm):
    title = forms.CharField(
        
        widget=forms.TextInput(
            attrs={"placeholder": "Company Name",}
        ),
    )
    desc = forms.CharField(
        
        widget=forms.Textarea(
            attrs={"placeholder": "share your experience",'style': 'height: 500px;width:500px'}
        ),
    )
    class Meta:
        model=Post
        fields=['title','desc']

class CommentForm(ModelForm):
    
    body = forms.CharField(
        
        widget=forms.Textarea(
            attrs={"placeholder": "Comment here",'style': 'height: 50px;width:500px'}
        ),
    )
    class Meta:
        model=Comment
        fields=['body']
       

        

class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        
        widget=forms.TextInput(
            attrs={"placeholder": "username",}
        ),
    )
    email = forms.CharField(
        
        widget=forms.TextInput(
            attrs={"placeholder": "email",}
        ),
    )
    password1 = forms.CharField(
        
        widget=forms.PasswordInput(
            attrs={"placeholder": "password",}
        ),
    )
    password2 = forms.CharField(
        
        widget=forms.PasswordInput(
            attrs={"placeholder": "re enter password",}
        ),
    )
    phone = forms.CharField(
        
        widget=forms.TextInput(
            attrs={"placeholder": "phone",}
        ),
    )
    section = forms.CharField(
        label='Section',
        widget=forms.Select(choices=s),
    )
    branch=forms.CharField(label='Branch', widget=forms.Select(choices=b))
    
    class Meta:
        model=User
        fields=["username",'email','password1','password2','phone','section','branch']
    
