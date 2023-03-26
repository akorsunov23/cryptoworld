from cryptocurrencies.models import Cryptocurrencies
from rest_framework import serializers


class CryptocurrenciesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cryptocurrencies
		fields = ['base_name', 'product_id', 'price', 'price_percentage_change_24h', 'volume_24h', 'added']
