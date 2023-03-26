from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Favorites(models.Model):
	user_pk = models.IntegerField(null=False, blank=False, verbose_name='id_пользователя')
	slug = models.SlugField(max_length=100, null=False, blank=False, verbose_name='Слаг')
	cryptocurrencies = models.ForeignKey('Cryptocurrencies', on_delete=models.PROTECT)


class Cryptocurrencies(models.Model):
	base_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='наименование')
	product_id = models.CharField(max_length=100, null=False, blank=False, verbose_name='символьный код')
	price = models.CharField(max_length=100, null=False, blank=False, verbose_name='тариф')
	price_percentage_change_24h = models.CharField(
		max_length=100, null=False, blank=False, verbose_name='изменение за 24ч'
	)
	volume_24h = models.CharField(max_length=100, null=False, blank=False, verbose_name='объём продаж')
	added = models.DateTimeField(default=datetime.now(), auto_created=True, verbose_name='добавлено в БД')

	class Meta:
		ordering = '-price',
