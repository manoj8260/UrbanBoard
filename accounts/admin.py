from django.contrib import admin
from accounts.models import User ,Profile
from django.contrib.auth.admin import UserAdmin
# Register your models here.
print('hello')
class UserModelAdmin(UserAdmin):
    model = User
    list_display = ['id','email','username','phone','is_active','is_staff','is_superuser',]
    list_filter =['is_superuser']
    search_fields = ['email','phone']
    ordering = ['id','email']
    filter_horizontal = ()
    readonly_fields =['date_joined','date_updated']

    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'phone','role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login','date_joined', 'date_updated' )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
admin.site.register(User,UserModelAdmin)
admin.site.register(Profile)    