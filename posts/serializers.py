from rest_framework import serializers
from .models import RacePost

class RacePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RacePost
        fields = ['id', 'title', 'description', 'distance', 'elevation']