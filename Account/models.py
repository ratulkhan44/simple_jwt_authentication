from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,**kwargs):
        print('8888888888888888888888888888888888888')
        if not kwargs.get('email'):
            raise ValueError('User must be needed a email address.')
        if not kwargs.get('password'):
            raise ValueError('User must be needed a password for security issue.')
        
        user_obj = self.model(
            email=self.normalize_email(kwargs.pop('email'))
        )
        user_obj.set_password(kwargs.pop('password'))

        for k, v in kwargs.items():
            setattr(user_obj, k, v)

        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, email, password=None):
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True
        )
        return user




class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(_('first name'),max_length=30, null=True, blank=True)
    last_name = models.CharField(_('last name'),max_length=30, blank=True, null=True)
    user_name = models.CharField(_('user name'),max_length=30)
    email = models.EmailField(_('email'),unique=True)  
    is_active = models.BooleanField(_('active'),default=True),
    is_staff = models.BooleanField(_('staff'),default=False)
    is_admin = models.BooleanField(_('admin'),default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    objects = UserManager()

    USERNAME_FIELD = 'email'  # username

    # USERNAME_FIELD and email are required by default
    REQUIRED_FIELDS = []  # ['full_name', 'email']


    def __str__(self):
        return self.email

    def get_user(self):
        return self.email

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name or "")

    def short_name(self):
        if self.first_name:
            return self.first_name
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        

class Book(models.Model):
    name = models.CharField(_('book name'),max_length=30, null=True, blank=True)     
    author = models.CharField(_('author'),max_length=30, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
