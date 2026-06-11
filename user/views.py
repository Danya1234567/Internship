
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.pagination import Pagination
from user.models import User
from user.serializer import RegisterSerializer, LoginSerializer, UserSerializer


# Create your views here.
class Register(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    serializer_class=LoginSerializer
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.validated_data['user']
            token,created=Token.objects.get_or_create(user=user)
            return Response({"token Given":token.key},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Verify(APIView):
    def get(self, request):
        return Response({"message": "Verification Successful"}, status=status.HTTP_200_OK)


class getMe(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class getAll(APIView):

    permission_classes=[IsAdminUser]
    def get(self,request):
        user=User.objects.all().order_by('id')
        paginator=Pagination()
        results=paginator.paginate_queryset(user,request)
        serializer=UserSerializer(results,many=True)
        return paginator.get_paginated_response(serializer.data)


class getUser(APIView):
    def get_object(self,request,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self,request,pk):
        user=self.get_object(request,pk)
        if not user:
            return Response({"message":"User does not exist"},status=status.HTTP_404_NOT_FOUND)
        serializer=UserSerializer(user)
        return Response(serializer.data)

    def patch(self,request,pk):
        user=self.get_object(request,pk)
        if not user:
            return Response({"message":"User does not exist"},status=status.HTTP_404_NOT_FOUND)
        serializer=UserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class DeleteUser(APIView):
    def delete(self,request,pk):
        try:
            user=User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"message":"User does not exist"},status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
