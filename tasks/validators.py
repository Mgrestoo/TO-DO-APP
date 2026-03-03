import re 
from django import forms

def validate_password(value):
    if len(value) < 8:
        raise forms.ValidationError('Password must be atleast 8 characters.')
    
    if not re.search(r'[a-zA-Z]', value):
        raise forms.ValidationError('Password must contain atleast one letter.')
    if not re.search(r'[0-9]', value):
        raise forms.ValidationError('Password must contain atleast one number.')
    if not re.search(r'[!@#$%^&*()_+=\-\[\]{};:\'",.<>?/\\|`~]', value):
        raise forms.ValidationError('Password must contain atleast one special character.')

