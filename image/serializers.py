from .models import  Image_u
from rest_framework import serializers



class Image_usSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image_u
        # fields= '__all__'
        fields= ['id','image', 'title', 'product_description', 'price']