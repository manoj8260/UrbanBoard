from django import forms
from .models import User
from django.core.exceptions import ValidationError
class Signupform(forms.ModelForm):
    confirm_password=forms.CharField(
         help_text =' Password must match the one above.',
         widget=forms.PasswordInput(
         attrs={
              'placeholder' : 'Confirm Password'
              
         }
    ))
    class Meta:
        model=User
        fields=('email','username','phone','password','role')
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
        help_texts = {'password' :'Choose  a strong password'}
    def clean(self):
            cleaned_data=super().clean()
            pswd=cleaned_data.get('password')
            cpswd=cleaned_data.get('confirm_password')
            if pswd!=cpswd:
                raise ValidationError('Password does not match, try again!')
            return cleaned_data
        


class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        help_text="Enter your registered email or phone number.",
        widget=forms.TextInput(attrs={
            'placeholder': 'Email or Phone',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        label="" ,
        help_text="Enter your account password.",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        })
    )

    