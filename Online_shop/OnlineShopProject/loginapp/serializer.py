from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    """ Serializer for Address"""
    class Meta:
        model = Address
        fields = ('id', 'city', 'address', 'zip_number')

    def create(self, validated_data):
        user = self.context['request'].user
        city = validated_data['city']
        address = validated_data['address']
        zip_number = validated_data['zip_number']
        address =Address(user=user, city=city, address=address, zip_number=zip_number)
        address.save()
        return address
