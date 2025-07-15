from django.contrib import admin
from .models import PGlisting
# Register your models here.

class PGCustomAdmin(admin.ModelAdmin):
    model = PGlisting
    list_display = ['owner','title','location']
    
admin.site.register(PGlisting,PGCustomAdmin)