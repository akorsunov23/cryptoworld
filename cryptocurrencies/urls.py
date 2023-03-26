from django.urls import path
from cryptocurrencies.views import ProductView, FavoritesView

app_name = 'cryptocurrencies'

urlpatterns = [
	path('all_product/', ProductView.as_view(), name='all_product'),
	path('favorites/<slug:slug>/', FavoritesView.as_view(), name='favorites'),
]
