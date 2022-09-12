from fcntl import F_DUPFD
from django.shortcuts import render
from django.http import JsonResponse
from .models import Crypto, Nft, User
from rest_framework import generics
from .serializers import CryptoSerializer, NftSerializer, UserSerializer

# Create your views here.


class CryptoList(generics.ListCreateAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer


class CryptoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crypto.ojects.all()
    serializer_class = CryptoSerializer


class NftList(generics.ListCreateAPIView):
    queryset = Nft.objects.all()
    serializer_class = NftSerializer


class NftDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nft.ojects.all()
    serializer_class = NftSerializer
