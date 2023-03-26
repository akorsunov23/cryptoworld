from cryptocurrencies_api.api import FavoritesListView, FavoritesView
from django.urls import path

app_name = 'cryptocurrencies_api'

urlpatterns = [
	path('favorites/', FavoritesListView.as_view(), name='favorites_list'),
	path('favorites/detail/<name_id>/', FavoritesView.as_view(), name='favorites_detail')
]

