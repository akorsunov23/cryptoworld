from cryptocurrencies.models import Favorites
from rest_framework import serializers


class FavoritesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Favorites
		fields = ['id', 'user_pk', 'name', 'name_id', 'price', 'created_at']
