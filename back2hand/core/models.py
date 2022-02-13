from django.db import models
from  django.conf import settings
import uuid

from django.utils import  timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.




def upload_to(instance, filename):
    return 'ImgProduct/{filename}'.format(filename=filename)

def upload_to2(instance, filename):
    return 'Test/{filename}'.format(filename=filename)

def imageProduct2(instance, filename):
   return 'imageProduct2/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return  f'{self.id ,self.name}'  

class Product(models.Model):
    code = models.CharField(max_length =10, unique=True ,primary_key=True)
    producer = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.code



class Detail(models.Model):
    code = models.ForeignKey(Product, on_delete=models.CASCADE)
    category =  models.ForeignKey(Category,on_delete= models.PROTECT ,blank=True , null=True)
    title = models.CharField(max_length=100 , blank=False)
    synopsis = models.TextField()
    choice_language =(
        ('english','english'),
        ('thai','thai')
    )
    language = models.CharField(choices= choice_language , max_length=10)
    price = models.CharField(max_length=3)
    originalPrice = models.CharField(max_length=3)
    isbn = models.CharField(max_length=10)
    pageNumber = models.CharField(max_length=3)
    slug = models.SlugField(max_length=100)
    quantity = models.CharField(max_length=3)
    imgProduct = models.ImageField(_("ImgProduct"),upload_to=upload_to)
    imgProduct2 = models.ImageField(_("imageProduct2"),upload_to = imageProduct2 , null = True ,blank=True)
    author = models.CharField(max_length=50)
    choice_status = (
        ('on','on'),
        ('off','off')
    )
    status = models.CharField(choices=choice_status, max_length=3 ,default='off')
  


    def __str__(self):
        return self.title 


class Invoice(models.Model):
     invoiceNo =  models.UUIDField(primary_key=True , default=uuid.uuid4 , editable= False)
     indate = models.DateTimeField(default=timezone.now)
     customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class InvoiceItem(models.Model):
    invoiceNo = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=3)
    itemNo = models.ForeignKey(Product,on_delete=models.CASCADE)



class TestImage2(models.Model):
     image = models.ImageField(
        _("Test2"), upload_to=upload_to2)















    
