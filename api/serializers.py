from rest_framework import serializers
from teammatcherapp import models
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only': True},
            'username' : {'write_only': True}
            }

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeaderBoardPosition
        fields = '__all__'
        
