from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Type


class TypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('url', 'name')