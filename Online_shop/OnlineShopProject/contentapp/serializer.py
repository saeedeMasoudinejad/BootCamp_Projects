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
        fields = ('id', 'name', 'img', 'price', 'brand', 'existance_status')


class AllTvSerializer(HyperlinkedModelSerializer):
    """" Serializer for show all Tv with summery information"""
    class Meta:
        model = TV
        fields = ('url', 'name', 'img')

class AllMobileSerializer(HyperlinkedModelSerializer):
    """" Serializer for show all Mobile with summery information"""
    class Meta:
        model = Mobile
        fields = ('url', 'name', 'img')


class AllLaptopSerializer(HyperlinkedModelSerializer):
    """" Serializer for show all Laptop with summery information"""
    class Meta:
        model = Laptop
        fields = ('url', 'name', 'img')

class AllRefrigeratorSerializer(HyperlinkedModelSerializer):
    """" Serializer for show all Refrigerator with summery information"""
    class Meta:
        model = Refrigerator
        fields = ('url', 'name', 'img')


class EachTvInfSerializer(ModelSerializer):
    """" Serializer for all information of each Tv"""

    class Meta:
        model = TV
        fields = '__all__'

class EachMobileInfSerializer(ModelSerializer):
    """" Serializer for all information of each Mobile"""

    class Meta:
        model = Mobile
        fields = '__all__'


class EachLaptopInfSerializer(ModelSerializer):
    """" Serializer for all information of each Laptop"""

    class Meta:
        model = Laptop
        fields = '__all__'


class EachRefrigeratorInfSerializer(ModelSerializer):
    """" Serializer for all information of each Refrigerator"""

    class Meta:
        model = Refrigerator
        fields = '__all__'