from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager ,PermissionsMixin
import re
from django.core.exceptions import ValidationError


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,phone,password=None,**extra_fields):
        if not email or not phone:
            raise ValueError('Both email and phone number must be provided.')
        user=self.model(email=self.normalize_email(email),phone = phone,**extra_fields)
        user.set_password(password)
        # user.is_active=True
        user.save(using=self._db)
        return user
    def create_superuser(self,email,phone,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be True')
        if not email or not phone:
            raise ValueError('Superuser requires both email and phone number.')
        user=self.create_user(email,phone,password,**extra_fields)
        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)
        return user
class User(AbstractBaseUser,PermissionsMixin):
    class Role(models.TextChoices):
        LANDLORD = 'landlord', 'Landlord'
        BOARDER = 'boarder', 'Boarder'

    def validate_phone(value):
        pattern = r'^[6-9]\d{9}$'  # Indian 10-digit mobile starting with 6-9
        if not re.match(pattern, value):
            raise ValidationError("Enter a valid 10-digit Indian phone number.")
        
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=15,verbose_name= 'Phone Number', unique=True,validators=[validate_phone])
    username=models.CharField(max_length=200,null=True,blank=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    role = models.CharField(max_length=50,choices=Role.choices,default=Role.BOARDER)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['phone']

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        if self.is_superuser:
            return True
        return super().has_perm(perm,obj)
    
    def has_module_perms(self,app_label):
        if self.is_superuser:
            return True
        return super().has_module_perms(app_label)
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
class Profile(models.Model):
    genders = [
        ('Male' , 'Male'),
        ('Female' ,'Female'),
        ('Other' ,'Other'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(null=True,blank=True)
    profile_pic=models.ImageField(upload_to='profiles/',blank=True,null=True)
    gender = models.CharField(max_length=50,choices=genders,blank=True,null=True)

    def __str__(self):
        return f'Profile :- {self.user.username}'     