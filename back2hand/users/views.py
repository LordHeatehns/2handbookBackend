from django.contrib.auth.models import Permission
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from users.models import NewUser




# Create your views here.

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self , request):
        password = request.data['password']
        confirm = request.data['confirmpassword']
        email = request.data['email']
        username = request.data['user_name']
        reg_serializer =  CustomUserSerializer(data = request.data)
        if confirm == password :
           if NewUser.objects.filter(email = email).exists():
               print('email not')
               result = {'mesemail':'email is alreadt in use'}
               return JsonResponse(result)
           elif NewUser.objects.filter(user_name =  username).exists():
               print('user not')
               result = {'mesuser':'user is already in use'}
               return JsonResponse(result)
           elif reg_serializer.is_valid():
            newuser = reg_serializer.save()
            print(reg_serializer)
            if newuser:
                return Response(status = status.HTTP_201_CREATED)
        else:
            print('password not')
            result = {'mesconfirmpassword':"password isn't matching"}
            return JsonResponse(result)

        return Response(reg_serializer.errors, status =status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authenthication_classes = ()

    def post(self, request):

        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            print(refresh_token)
            print('logout')
            return Response(status = status.HTTP_205_RESET_CONTENT)
        
        except Exception as error :
            print(f'{error} + 55')
            return Response(status = status.HTTP_400_BAD_REQUEST)



