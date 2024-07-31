from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer,UserLoginSerializer,ForgotPasswordSerializer,ChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from .models import CustomUser
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token_data = get_tokens_for_user(user)
            return Response(token_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request,email=email,password=password)
            if user is None:
                return Response({"message":"Invalid Email or Password"},status=status.HTTP_400_BAD_REQUEST)
            token = get_tokens_for_user(user)
            return Response({
                "message":"Login Success",
                "token":token,
                "email":user.email,
                "isAdmin":user.is_admin
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ForgotPasswordView(APIView):
    def post(self,request):
        serializer = ForgotPasswordSerializer(data=request.data)

        if serializer.is_valid(): 
            email = serializer.validated_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user :
                link = f"http://127.0.0.1:3000/change-password/{user.id}/"
                send_mail(
                    subject="Forgot Password",
                    message=f"Click the following to reset your password {link}",
                    from_email="ekoyi.org@gmail.com",
                    recipient_list=[email]
                )
                return Response({"message":"Please check your email"},status=status.HTTP_200_OK)
            return Response({"message":"User doesnot exists"},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ChangePasswordView(APIView):
   def put(self,request,id):
       serializer = ChangePasswordSerializer(data=request.data)
       if serializer.is_valid():
           password = serializer.validated_data['password']
           user = CustomUser.objects.get(id=id)
           user.set_password(password)
           user.save()
           return Response({"message":"Successfully updated Password "},status=status.HTTP_200_OK)
       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)           
    