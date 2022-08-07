
from dataclasses import field
from re import A
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth.models import AbstractUser

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'



class Popform(forms.ModelForm):
    def __init__(self, *args,  **kwargs): 
            super().__init__(*args, **kwargs)
            self.fields["prove_of_payment"].widget.attrs.update({
                'required': '',
                'name':'prove_of_payment'
        })
    class Meta:
        model = Pop
        fields = ['prove_of_payment']
        


class RegisterForm(UserCreationForm):
    def __init__(self, *args,  **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required': '',
            'name':'usermame',
            'id':'username',
            'type':'text',
            'class':'form-input',
            'placeholder': 'Create a user name',
            'maxlenght':'16',
            'minlenght':'6'
        })
        self.fields["email"].widget.attrs.update({
            'required': '',
            'name':'email',
            'id':'email',
            'type':'email',
            'class':'form-input',
            'placeholder': 'Enter your email',
            'maxlenght':'16',
            'minlenght':'6'
        })
        self.fields["first_name"].widget.attrs.update({
            'required': '',
            'name':'first_name',
            'id':'first_name',
            'type':'text',
            'class':'form-input',
            'placeholder': 'First name',
            'maxlenght':'16',
            'minlenght':'6'
        })
        self.fields["last_name"].widget.attrs.update({
            'required': '',
            'name':'last_name',
            'id':'last_name',
            'type':'text',
            'class':'form-input',
            'placeholder': 'Last name',
            'maxlenght':'16',
            'minlenght':'6'
        })
        self.fields["password1"].widget.attrs.update({
            'required': '',
            'name':'password1',
            'id':'password1',
            'type':'text',
            'class':'form-input',
            'placeholder': 'password',
            'maxlenght':'22',
            'minlenght':'8'
        })
        self.fields["password2"].widget.attrs.update({
            
            'required': '',
            'name':'password2',
            'id':'password2',
            'type':'text',
            'class':'form-input',
            'placeholder': 'Confirm password',
            'maxlenght':'22',
            'minlenght':'8'
        })
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
        
class login_user(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'username',}
        ), label='username')
    
    class login_user(AuthenticationForm):
        username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'username',}
        ), label='username')
        
class CustomerForm(ModelForm):
    def __init__(self, *args,  **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            'required': '',
            'name':'email',
            'id':'email',
            'type':'text',
            'class':'form-input',
            'placeholder': 'Edit your email',
            'maxlenght':'20',
            'minlenght':'11'
        })
        self.fields["phone"].widget.attrs.update({
            'required': '',
            'name':'phone',
            'id':'phone',
            'type':'text',
            'class':'form-input',
            'placeholder': 'edit phone number',
            'maxlenght':'11',
            'minlenght':'11'
        })
        self.fields["profile_pic"].widget.attrs.update({
            'required': '',
            'name':'profile_pic',
            'id':'profile_pic'
        })
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'name']   
            

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('commenter_name', 'comment_body')
#         widgets = {
#             'commenter_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ignor if logged in'}),
#             'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
#         }




