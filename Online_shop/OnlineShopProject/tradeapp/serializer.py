from rest_framework import serializers
from .models import Cart, Order
from contentapp.models import Content
from contentapp.serializer import ContentSerializer
from loginapp.models import Address
from loginapp.serializer import AddressSerializer
from rest_framework.response import Response


class CartSerializer(serializers.Serializer):
    """" Serializer for get the order user want add, update in her cart, use the defult of delete function of Serializers"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    good = serializers.PrimaryKeyRelatedField(required=True, queryset=Content.objects.all())
    num = serializers.IntegerField(min_value=1, required=True)

    def create(self, validated_data):
        user = self.context['request'].user
        good = validated_data['good']
        num = validated_data['num']

        if good.inventory >= num:
            exist_user_good = Cart.objects.filter(user=user, good=good, status='c')
            if len(exist_user_good) == 0:
                exist_user_good = Cart.objects.create(**validated_data)
            else:
                exist_user_good = exist_user_good[0]
                if num > 0:
                    exist_user_good.num += num
                    exist_user_good.save()
                elif num == 0:
                    exist_user_good.delete()

            return exist_user_good
        else:
            raise serializers.ValidationError("This good doesn't exist enough")

    """" To Do: can update the value"""
    def update(self, instance, validated_data):
        if instance.good.inventory >= validated_data['num']:
            instance.num = validated_data['num']
            instance.save()
        else:
            if instance.good.inventory > 0:
                raise serializers.ValidationError("{} is exist just {}".format(instance.good.name,
                                                                               instance.good.inventory))
            else:
                instance.delete()
                raise serializers.ValidationError("{} doesn't exist, so remove it from your cart".format
                                                  (instance.good.name))
        return instance


class CartDetailSerializer(serializers.ModelSerializer):
    """ Serialize the each record of cart"""
    good = ContentSerializer(many=False)

    class Meta:
        model = Cart
        fields = ('good', 'num')


class OrderSerializer(serializers.Serializer):
    """serializer for confirm the order is exist in user cart"""
    confirmation_status = serializers.ChoiceField(choices=['confirm', 'reject'])


class ChoiceAddressSerializer(serializers.Serializer):
    """"serializer for choice the address want user's order send"""
    address_id = serializers.IntegerField(min_value=1, required=True)


class FinalFactorSerializer(serializers.ModelSerializer):
    """ serializer for final factor"""
    address = AddressSerializer(many=False)

    class Meta:
        model = Order
        fields = ('id', 'goods', 'address', 'sum_price', 'supplier_status')


class PaymentSerializer(serializers.Serializer):
    """" for verify payment"""
    confirmation_status = serializers.ChoiceField(choices=['pay', 'reject'])


class SupplierSerializer(serializers.Serializer):
    """" for verify of factor"""
    factor_id = serializers.IntegerField(min_value=1)
    confirmation_status = serializers.ChoiceField(choices=['verify', 'reject'])

    def create(self, validated_data):
        if validated_data['confirmation_status'] == 'verify':
            id = validated_data['factor_id']
            factor_obj = Order.objects.get(id=id)
            factor_obj.supplier_status = 'v'
            factor_obj.save()
        return validated_data
