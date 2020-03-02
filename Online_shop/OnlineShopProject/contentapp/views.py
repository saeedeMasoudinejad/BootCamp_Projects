from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import (AllTvSerializer, AllMobileSerializer, AllLaptopSerializer,
                         AllRefrigeratorSerializer, EachLaptopInfSerializer, EachMobileInfSerializer,
                         EachRefrigeratorInfSerializer, EachTvInfSerializer)
from .models import TV, Mobile, Laptop, Refrigerator
from rest_framework import filters


class ShowAllTv(ReadOnlyModelViewSet):

    queryset = TV.objects.all()
    serializer = {
        'list': AllTvSerializer,
        'retrieve': EachTvInfSerializer
    }
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )

    def get_serializer_class(self):
        return self.serializer.get(self.action)


class ShowAllMobile(ReadOnlyModelViewSet):

    queryset = Mobile.objects.all()
    serializer = {
        'list': AllMobileSerializer,
        'retrieve': EachMobileInfSerializer
    }
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )

    def get_serializer_class(self):
        return self.serializer.get(self.action)


class ShowAllLaptop(ReadOnlyModelViewSet):

    queryset = Laptop.objects.all()
    serializer = {
        'list': AllLaptopSerializer,
        'retrieve': EachLaptopInfSerializer
    }
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )

    def get_serializer_class(self):
        return self.serializer.get(self.action)


class ShowAllRefrigerator(ReadOnlyModelViewSet):

    queryset = Refrigerator.objects.all()
    serializer = {
        'list': AllRefrigeratorSerializer,
        'retrieve': EachRefrigeratorInfSerializer
    }
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )

    def get_serializer_class(self):
        return self.serializer.get(self.action)


# class DetailsShowContent(APIView):
#     def get(self, request, id):
#         type = Type.objects.get(id=id)
#         return Response(type['type_name'])

# class ShowType(ReadOnlyModelViewSet):
#     queryset = Type.objects.all()
#     serializer_class = TypeSerializer