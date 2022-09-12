from rest_framework import serializers
from .models import Crypto, Nft


class CryptoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    class Meta:
        model = Crypto
        fields = ('id', 'user', 'name', 'amount')


class NftSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    class Meta:
        model = Nft
        fields = ('id', 'user', 'name', 'blockchain', 'photo')
