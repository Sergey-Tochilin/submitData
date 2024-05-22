from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'fam', 'name', 'otc', 'phone']

class CoordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'spring', 'summer', 'autumn']

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['data', 'title']

class PerevalSerializer(WritableNestedModelSerializer):
    user = MyUserSerializer
    coords = CoordsSerializer
    level = LevelSerializer
    image = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['beauty_name', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level', 'status']