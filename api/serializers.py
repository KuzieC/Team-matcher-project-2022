from rest_framework import serializers
from teammatcherapp import models
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'city',
            'name',
            'gender',    
            'phone',
            'age',
            'sport',
            'experience',
            'mode',
        )
        model = models.User