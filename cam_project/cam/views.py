from fcntl import F_DUPFD
from django.shortcuts import render
from django.http import JsonResponse
from .models import Crypto, Nft

# Create your views here.


def crypto_list(request):
    cryptos = Crypto.objects.all().values('user', 'name', 'amount')
    cryptos_list = list(cryptos)
    return JsonResponse(cryptos_list, safe=False)


def nft_list(request):
    nfts = Nft.objects.all().values('user', 'name', 'blockchain', 'photo')
    nfts_list = list(nfts)
    return JsonResponse(nfts_list, safe=False)
