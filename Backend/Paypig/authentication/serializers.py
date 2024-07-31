from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = CustomUser
        fields =['email','password','password2','price']

    def validate(self,attrs):
         if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password2": "Passwords does not matched!!."})
         if len(attrs['password']) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})
         if CustomUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email already exists."})
         return attrs
    
    def create(self,validated_data):
        user = CustomUser.objects.create(
            email = validated_data['email'],
            price = validated_data['price']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255,write_only=True)

    def validate(self,attrs):
        email = attrs.get("email",None)
        password = attrs.get("password",None)

        if email is None:
            raise serializers.ValidationError("Email should required for login")
        if password is None:
            raise serializers.ValidationError("Password should required for login")
        return attrs
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,write_only=True)
    password1 = serializers.CharField(max_length=255,write_only=True)

    def validate(self, attrs):
        password = attrs.get("password")
        password1 = attrs.get("password1")
        print(password)
        print(password1)
        if password!=password1:
            raise serializers.ValidationError("Password does not matching")
        return attrs