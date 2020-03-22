from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializer import (AllTvSerializer, AllMobileSerializer, AllLaptopSerializer,
                         AllRefrigeratorSerializer, EachLaptopInfSerializer, EachMobileInfSerializer,
                         EachRefrigeratorInfSerializer, EachTvInfSerializer)
from .models import TV, Mobile, Laptop, Refrigerator
from rest_framework import filters


class ShowAllTv(ReadOnlyModelViewSet):
    """ show all Tv with some detail and all detail info of each Tv """
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
    """ show all Mobile with some detail and all detail info of each Mobile """
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
    """ show all laptop with some detail and all detail info of each laptop """
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
    """ show all Refrigerator with some detail and all detail info of each Refrigerator """
    queryset = Refrigerator.objects.all()
    serializer = {
        'list': AllRefrigeratorSerializer,
        'retrieve': EachRefrigeratorInfSerializer
    }
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )

    def get_serializer_class(self):
        return self.serializer.get(self.action)


