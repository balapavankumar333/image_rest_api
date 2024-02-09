from rest_framework import serializers
from .models import CatPicture

class CatPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatPicture
        fields = '__all__'
