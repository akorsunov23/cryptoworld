from django.contrib.auth.models import User
from django.db import models


class Favorites(models.Model):
	user_pk = models.IntegerField(null=False, blank=False, verbose_name='id_пользователя')
	slug = models.SlugField(max_length=100, null=False, blank=False, verbose_name='Слаг')
	cryptocurrencies = models.ForeignKey('Cryptocurrencies', on_delete=models.PROTECT)


class Cryptocurrencies(models.Model):
	base_name = models.CharField(max_length=100, null=False, blank=False)
	product_id = models.CharField(max_length=100, null=False, blank=False)
	price = models.CharField(max_length=100, null=False, blank=False)
	price_percentage_change_24h = models.CharField(max_length=100, null=False, blank=False)
	volume_24h = models.CharField(max_length=100, null=False, blank=False)

	class Meta:
		ordering = '-price',
