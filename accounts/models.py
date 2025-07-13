from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Must have valid email')
        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        # user.is_active=True
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be True')
        user=self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    email=models.EmailField(max_length=200,unique=True)
    username=models.CharField(max_length=200)
    phone=models.CharField(max_length=15,null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    profile_pic=models.ImageField(upload_to='profiles/',blank=True,null=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_landlord=models.BooleanField(default=False)
    is_boarder=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    objects=UserManager()
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    def has_module_perms(self,app_label):
        return self.is_superuser