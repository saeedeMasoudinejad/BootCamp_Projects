from rest_framework import serializers
from .models import Cart
from contentapp.models import Content
from contentapp.serializer import ContentSerializer

class CartSerializer(serializers.Serializer):
    """" Serializer for get the order user want add in her cart"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    good = serializers.PrimaryKeyRelatedField(required=True, queryset=Content.objects.all())
    num = serializers.IntegerField(min_value=1, required=True)

    def create(self, validated_data):
        user = self.context['request'].user
        good = self.validated_data['good']
        num = self.validated_data['num']

        if good.inventory >= num:
            exist_user_good = Cart.objects.filter(user=user, good=good, status='c')
            if len(exist_user_good) == 0:
                exist_user_good = Cart.objects.create(**validated_data)
                good.inventory -= num
                good.save()
            else:
                exist_user_good = exist_user_good[0]
                exist_user_good.num += num
                good.inventory -= num
                exist_user_good.save()
                good.save()
            return exist_user_good


class CartDetailSerializer(serializers.ModelSerializer):
    good = ContentSerializer(many=False)
    class Meta:
        model = Cart
        fields = ('good', 'num')



