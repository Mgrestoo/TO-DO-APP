# from django import forms

from cProfile import label
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from django.http import request
from .models import Task, UserProfile
from .validators import validate_password

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'image')
        widgets = {
            'bio':forms.Textarea(attrs={
                'placeholder': 'Tell us about yourself',
                'rows': 4,
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Upload your profile picture',
                'accept': 'image/*'
            })
            
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Task description (optional)', 'rows': 4}),
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 4:
            raise forms.ValidationError('Title must have atleast four characters!!')
        return title    

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput , validators=[validate_password])
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password", )
    
    class Meta:
        model = User
        fields = ('username', 'email')
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username
    
 
    
    
     
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
    