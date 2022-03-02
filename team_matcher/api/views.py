import imp
from django.shortcuts import render
from itsdangerous import serializer
from rest_framework import generics, status
#from team_matcher.api.models import Person
from .serializers import PersonSerializer, CreateSearchSerializer
from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response

#takes a web request and returns a web response
# Create your views here.
class PersonView(generics.ListCreateAPIView): #allows us to view all persons -remove create
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

#class CreateSearchView(APIView): #NOT WORKING
    #serializer_class = PersonSerializer
    #def get(self, request, format = None):
        #serializer=self.serializer_class(data=request.data)
        #else: 
            #return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)



