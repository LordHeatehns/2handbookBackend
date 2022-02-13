from statistics import mode
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
from django.conf import settings
from PIL import Image
from django.utils.translation  import gettext_lazy 

from core.models import upload_to

# Create your models here.

def upload_to(instance, filename):
    return 'Test/{filename}'.format(filename=filename)

def upload_to_profile(instance, filename):
    return 'image_profile/{filename}'.format(filename=filename)

class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150 , unique= True)
    first_name = models.CharField(max_length=150 , blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500 , blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name


class ImageProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete= models.CASCADE  , related_name='tracks')
    image = models.ImageField(gettext_lazy('profile') ,upload_to = upload_to_profile,null =True ,default = 'default_image.jpg')

    def save(self , *args , **kwargs):
        super().save(*args , **kwargs)
        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100 :
            resized = (100,100)
            img.thumbnail(resized)
            img.save(self.image.path)



class TestImage(models.Model):
    image  = models.ImageField(gettext_lazy('testImage'),upload_to = upload_to, null = True )
   

    

    



