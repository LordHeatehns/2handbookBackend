
from rest_framework import serializers 
from .models import NewUser , ImageProfile


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required = True)
    user_name = serializers.CharField(required = True)
    password = serializers.CharField(min_length = 8 ,write_only = True)
    first_name = serializers.CharField(required = True)

    class Meta:
        model = NewUser
        fields = ('email','user_name','password','first_name')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None :
            instance.set_password(password)
        
        instance.save()
        return instance


class CustomUser(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['user_name']


class CustomImageProfile(serializers.ModelSerializer):
    user = CustomUser()
    class Meta:
        model = ImageProfile
        fields = ['id','user','image']
    
   



