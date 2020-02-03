from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import AllTvSerializer,EachTvInfSerializer
from .models import TV


# class ShowType(ReadOnlyModelViewSet):
#     queryset = Type.objects.all()
#     serializer_class = TypeSerializer


class ShowAllTv(ReadOnlyModelViewSet):
    queryset = TV.objects.all()
    serializer = {
        'list': AllTvSerializer,
        'retrieve': EachTvInfSerializer
    }

    def get_serializer_class(self):
        return self.serializer.get(self.action)


# class DetailsShowContent(APIView):
#     def get(self, request, id):
#         type = Type.objects.get(id=id)
#         return Response(type['type_name'])