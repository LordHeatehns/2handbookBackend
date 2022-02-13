from functools import partial
from re import search
from unicodedata import category
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.query import QuerySet
from django.shortcuts import render
from users.models import ImageProfile , NewUser  ,TestImage
from users.serializers import CustomImageProfile
from core.models import Product , Detail  ,Category ,TestImage2
from .serializers import DetailSerializer, MyProductSerializer , PostAddProductSerializer ,ImageUpdateSerializer, TestImageSerializer2
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated , AllowAny ,SAFE_METHODS ,BasePermission
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
import random
from rest_framework.parsers import MultiPartParser, FormParser ,FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters
# Create your views here.



class DetailList(generics.ListAPIView):
    
    serializer_class = DetailSerializer
    queryset = Detail.objects.all()


class DetailPostSingle(generics.RetrieveAPIView):

    serializer_class =DetailSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Detail, slug=item)

class ImageProfileAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomImageProfile
    
    

    def get_queryset(self):
        user = self.request.user.id
        print(user)
        print(self.request.user)
        
        return ImageProfile.objects.filter(user = user)

class DetailUser(generics.ListAPIView):
    permission =[IsAuthenticated]
    serializer_class = MyProductSerializer

    def get_queryset(self):
        list = []
        print(self.request.user)
        be = Product.objects.filter(producer = self.request.user)
        for i in be:
            list.append(i.code)
        print(list)
        print(Detail.objects.filter(code__in = list))
        return Detail.objects.filter(code__in = list)

class Test2(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser,FormParser]
    
    def post(self ,request, format=None):
      
        print(request.data)
        print(type(request.data['bb']))

       
        
        
        
            
        return Response(status=status.HTTP_200_OK)
       

'''class Test2Show(generics.ListAPIView):
    serializer_class = TestImageSerializer2
    queryset = TestImage2.objects.all()'''

class CreateProduct(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

       
    def rendom(self,number):
            p = 'P'
            randomed = random.randint(100000000,999999999)
            newCode = f'{p}{randomed}'
            if newCode in number:
                random(number)
            
            else:
                return newCode
        
    def post(self , request, format=None):
        
        print(request.data)
        request.data.update({})
       

        allCode = Product.objects.values_list('code')
        newNumber = self.rendom(allCode)
        
        createNewProduct = Product.objects.create(
            code = newNumber,
            producer = request.user,
            
        )
        createNewProduct.save()

        request.data.update({'code':newNumber})
        serializer = PostAddProductSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            Product.objects.filter(code = newNumber).delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)    

        
       
     
          
                   
               
class DeleteProduct(APIView):
    permission_classes = [IsAuthenticated]
    def post(self , request):
        print(request.data)
        be = Product.objects.filter(code =request.data['id'])
        be.delete()
        print(be)
        return Response(status=status.HTTP_200_OK)



class ProductSearch(generics.ListAPIView):
    #permission_classes =[IsAuthenticated]
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']



class UpdateStatus(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            Detail.objects.filter(code = request.data['code']).update(
            status = request.data['status']
        )

        except Exception as err:
           return Response(status = status.HTTP_400_BAD_REQUEST)

        else:
            return  Response(status =status.HTTP_200_OK)


class UpdateImageBlob(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser,FormParser]
    queryset = ImageProfile.objects.all()
    serializer_class =ImageUpdateSerializer
    
    def post(self ,request, format=None):
        print(request.data)
        print(type(request.data['image']))
        user = ImageProfile.objects.get(user = request.user)
        serializerForm = ImageUpdateSerializer(user,data = request.data, partial=True)
        if serializerForm.is_valid():
            serializerForm.save()
            return  Response(status =status.HTTP_200_OK)
        
        

        return  Response(status =status.HTTP_200_OK)

#categories

class CategoriesManga(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        return Detail.objects.filter(category = 2)

class CategoriesEducation(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        return Detail.objects.filter(category = 5)

class CategoriesNovel(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        return Detail.objects.filter(category = 1)

class CategoriesArticle(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        return Detail.objects.filter(category = 4)


class CategoriesComic(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        return Detail.objects.filter(category = 6)

class CategoriesKnowledge(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        return Detail.objects.filter(category = 3)
'''class DetailList(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = DetailSerializer
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Detail, slug=item)

    def get_queryset(self):
        return Detail.objects.all()

list = []
        print(self.request.user)
        be = Product.objects.filter(producer = self.request.user)
        for i in be:
            list.append(i.code)
        print(list)
        return Detail.objects.filter(code__in =list)

class DetailUser(viewsets.ModelViewSet):
    
    serializer_class = MyProductSerializer

    def get_queryset(self):
        list = []
        print(self.request.user)
        be = Product.objects.filter(producer = self.request.user)
        for i in be:
            list.append(i.code)
        print(list)
        print(Detail.objects.filter(code__in = list))
        return Detail.objects.filter(code__in = list)


class ImageProfileAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomImageProfile
    
    

    def get_queryset(self):
        user = self.request.user
        
        return ImageProfile.objects.filter(user = user)


#post

class CreateProduct(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = MyProductSerializer

    def rendom(self,number):
            p = 'P'
            self.randomed = random.randint(100000000,999999999)
            self.newCode = f'{p}{self.randomed}'
            if self.newCode in number:
                random(number)
            
            else:
                return self.newCode

    def create(self, request):
            self.array = []
      
      
            latenumber = Product.objects.values_list('code')
            for i in latenumber :
               self.array.append(i)
               print(self.array)
            self.newNumber = self.rendom(latenumber)
            
            
            be = Product.objects.create(
                code = self.newNumber,
                producer = request.user,
                status = request.data['published']
            )
            be.save()

            new = get_object_or_404(Product , code = self.newCode) 
            category = get_object_or_404(Category , id =1)
            print(request.data['image'])
            print(type(request.data['image']))
            newProduct = Detail.objects.create(
                title = request.data['title'],
                price = request.data['price'],
                imgProduct =request.data['image'],
                slug =request.data['title'],
                synopsis =request.data['synopsis'],
                language = request.data['language'],
                originalPrice = request.data['originalPrice'],
                isbn = request.data['isbn'],
                pageNumber = request.data['numberOfPage'],
                quantity = request.data['quantity'],
                code = new ,
                author = request.data['author'],
                category =category

            )

            newProduct.save()
            return Response(data="return data")
          

class TestImages(viewsets.ModelViewSet):
    serializer_class = TestImageSerializer
    querySet = TestImage.objects.all()
    parser_classes = [FileUploadParser]
    
  
    def create(self , request, format=None):
          file_obj = request.data['img']
          TestImage.objects.create(img = file_obj)
          return Response(data='good')


    def get_queryset(self):
        return  TestImage.objects.all()'''    










