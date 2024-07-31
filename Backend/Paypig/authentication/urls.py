from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView,LoginView,ForgotPasswordView,ChangePasswordView

urlpatterns=[
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('signup/',RegisterView.as_view(),name="signup"),
   path("login/",LoginView.as_view(),name="login"),
   path("forgot-password/",ForgotPasswordView.as_view(),name="forgot_password"),
   path("change-password/<uuid:id>/",ChangePasswordView.as_view(),name="forgot_password"),

]   