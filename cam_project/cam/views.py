from fcntl import F_DUPFD
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def crypto_list(request):
    cryptos = Crypto.objects.all().values('user', 'name', 'amount')
    cryptos_list = list(cryptos)
    return JsonResponse(cryptos_list, safe=False)
