from cryptocurrencies_api.api import CryptocurrenciesListView, CryptocurrenciesView
from django.urls import path

app_name = 'cryptocurrencies_api'

urlpatterns = [
	path('cryptocurrencies/', CryptocurrenciesListView.as_view(), name='cryptocurrencies_list'),
	path('cryptocurrencies/<product_id>/', CryptocurrenciesView.as_view(), name='cryptocurrencies_detail')
]

