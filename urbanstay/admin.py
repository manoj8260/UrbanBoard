from django.contrib import admin
from urbanstay.models import Flat
# Register your models here.

class FlatAdmin(admin.ModelAdmin):
    list_display = ['title','state','city']
    
admin.site.register(Flat,FlatAdmin)    