from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username


class Crypto(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='cryptos')
    name = models.CharField(max_length=50)
    amount = models.PositiveBigIntegerField(max_length=100)

    def __str__(self):
        return self.name


class Nft(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='nfts')
    name = models.CharField(max_length=100)
    blockchain = models.CharField(max_length=50)
    photo = models.TextField()

    def __str__(self):
        return self.name
