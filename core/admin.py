from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class UserAdmin(BaseUserAdmin):
    model=User
    list_display=('email', 'is_landlord', 'is_boarder', 'is_staff', 'is_active')
    list_filter=('is_landlord', 'is_boarder', 'is_staff','is_superuser')
    fieldsets=((None, {'fields': ('email', 'password','username')}),
        ('Roles', {'fields': ('is_landlord', 'is_boarder')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),)
    add_fieldsets=((None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_landlord', 'is_boarder', 'is_staff', 'is_active')}
        ),)
    filter_horizontal=[]
    search_fields=('email',)
    ordering=('email',)
admin.site.register(User,UserAdmin)