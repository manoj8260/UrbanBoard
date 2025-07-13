from django import forms
from .models import PGlisting

class PGlistingform(forms.ModelForm):
    class Meta:
        model=PGlisting
        fields=['title','location','rent','sharing_type','room_type','facilities']
        