from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializer import TypeSerializer
from .models import Type


class ShowType(ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer