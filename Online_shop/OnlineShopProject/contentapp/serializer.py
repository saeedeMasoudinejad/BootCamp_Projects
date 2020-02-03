from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField
from .models import Type, Mobile, Laptop, TV, Refrigerator, Content


class ContentSerializer(ModelSerializer):
    """" Serializer for Content table include of all goods"""
    brand = SerializerMethodField()

    def get_brand(self, brand):
        return brand.brand.name_brand

    class Meta:
        model = Content
        fields = ('id', 'name', 'img', 'price', 'brand')


class AllTvSerializer(HyperlinkedModelSerializer):
    """" Serializer for show all Tv with summery information"""
    class Meta:
        model = TV
        fields = ('url', 'name', 'img')


class EachTvInfSerializer(ModelSerializer):
    """" Serializer for all information of each Tv"""

    class Meta:
        model = TV
        fields = '__all__'
