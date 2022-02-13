from msilib.schema import Class
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from core.models import Product , Detail ,TestImage2
from users.models import ImageProfile, NewUser ,TestImage


class Detailextabstack(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['user_name']

class DetailNameUser(serializers.ModelSerializer):
    producer = Detailextabstack()
    class Meta:
        model = Product
        fields = ['code','producer']

class DetailSerializer(serializers.ModelSerializer):
    code = DetailNameUser()
    class Meta:
        model = Detail
        fields = ['id','title','price','imgProduct','imgProduct2','slug','synopsis','language','originalPrice'
        ,'isbn','pageNumber','quantity','code','author']


class MyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['id','title','slug','synopsis','isbn','code','author','status']



#Form


class PostAddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields =   ['title','price','imgProduct','imgProduct2','slug','synopsis','language','originalPrice'
        ,'isbn','pageNumber','quantity','code','author','status']
'''class TestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestImage
        fields = ['img']'''


class TestImageSerializer2(serializers.ModelSerializer):
    class Meta:
        model = TestImage2
        fields = ['image']


class ImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProfile
        fields = ['user','image']




#categories get

 


        



