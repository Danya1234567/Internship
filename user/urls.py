from django.urls import path
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import Register, Login, Verify, getMe, getAll, getUser, DeleteUser

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('verify/',Verify.as_view(),name='verify'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/',getMe.as_view(),name='me'),
    path('users/',getAll.as_view(),name='users'),
    path('user/<int:pk>/',getUser.as_view(),name='user'),
    path('user/change/<int:pk>/',getUser.as_view(),name='change'),
    path('user/delete/<int:pk>/',DeleteUser.as_view(),name='delete'),
]