from django import forms
from .models import User
from django.core.exceptions import ValidationError
class Signupform(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('email','username','password','role')
        widgets={
            'password':forms.PasswordInput()
        }
    def clean(self):
            cleaned_data=super().clean()
            pswd=cleaned_data.get('password')
            cpswd=cleaned_data.get('confirm_password')
            is_landlord=cleaned_data.get('is_landlord')
            is_boarder=cleaned_data.get('is_boarder')
            if pswd!=cpswd:
                raise ValidationError('Password does not match, try again!')
            if is_landlord and is_boarder:
                raise ValidationError('Choose one option')
            elif not is_landlord and not is_boarder:
                raise ValidationError('You must choose one role')
            return cleaned_data
        
class Loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)