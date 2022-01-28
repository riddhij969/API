from django.shortcuts import render, HttpResponse

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import users
from .serializers import usersSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *
import oauth2
from django.template import loader
from django.views.generic import TemplateView

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# class usersList(ListAPIView):
#     users1 = users.objects.all()
#     serializer = usersSerializer
#     pagination_class = PageNumberPagination
#     filter_backends = [SearchFilter,OrderingFilter]
#     search_fields = ['firstname','lastname']

# class usersList(APIView):
#     def get(request):
#         users1 = users.objects.all()
#         serializer = usersSerializer(users1,many=True)
#         return Response(serializer.data)

class Users(ListAPIView):
    queryset = users.objects.all()
    serializer_class = usersSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['firstname']
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name__last_name']

# class UserAuthentication(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request':request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token= Token.objects.get_or_create(user=user)
#         return Response(token.key)



class usersList(APIView):

    def get(self,request):
        users1 = users.objects.all()
        serializer = usersSerializer(users1,many=True)
        return Response(serializer.data)


    def post(self,request):
        # pass
        serializer = usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class usersDetail(APIView):

    def get_user(self, first_name):
        try:
            users1 = users.objects.get(id = first_name)
            return users1
        except users.DoesNotExist:
            return

    def get(self,request, first_name):
        if not self.get_user(first_name):
            return Response(f'User with {first_name} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = usersSerializer(self.get_user(first_name))
        return Response(serializer.data)

    def put(self, request, first_name):
        if not self.get_user(first_name):
            return Response(f'User with {first_name} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = usersSerializer(self.get_user(first_name), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, first_name):
        if not self.get_user(first_name):
            return Response(f'User with {first_name} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        users1 = self.get_user(first_name)
        users1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)