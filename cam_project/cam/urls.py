from django.urls import path
from . import views

urlpatterns = [
    path('cryptos', views.crypto_list, name='crypto_list'),
    path('cryptos/<int:pk>', views.crypto_detail, name='crypto_detail'),
    path('nfts', views.nft_list, name='nft_list'),
    path('nfts/<int:pk>', views.nft_detail, name='nft_detail')
]
