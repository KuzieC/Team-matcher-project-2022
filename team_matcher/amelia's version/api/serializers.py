#takes a model and translates it to a JSON response 
import imp
from rest_framework import serializers
from .models import Person
from .models import Search

class PersonSerializer(serializers.ModelSerializer): #takes a room object and turns it into something we an send back as a response
    class Meta:
        model = Person
        fields = ('id', 'name', 'postcode', 'male', 'phone', 'age', 'sport', 'experience',  'username', 'password')

class CreateSearchSerializer(serializers.ModelSerializer): #takes a request and makes sure it is valid (?)
    class Meta:
        model = Search
        fields = ('postcode', 'sport',  'mode')