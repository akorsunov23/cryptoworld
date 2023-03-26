from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import ListView
from cryptocurrencies.models import Favorites
from cryptocurrencies.models import Cryptocurrencies


class ProductView(ListView):
	"""
	Выводит полный список найденных криптовалют по API и информацию о ней.
	Если в поле поиска задать значение, будет проведена фильтрация.
	"""
	context_object_name = 'products'
	paginate_by = 5
	template_name = 'cryptocurrencies/search_product.html'

	def post(self, request: HttpRequest):
		if 'product' in request.POST:
			crypt = Cryptocurrencies.objects.get(pk=self.request.POST.get('product'))
			Favorites.objects.create(
				user_pk=self.request.user.pk,
				cryptocurrencies=crypt,
				slug=self.request.user.username
			)
		return redirect('cryptocurrencies:all_product')

	def get_queryset(self, **kwargs):
		search = self.request.GET.get('search')

		if search and search == search.upper():
			products = Cryptocurrencies.objects.filter(product_id=search)
		elif search:
			products = Cryptocurrencies.objects.filter(base_name=search)
		else:
			products = Cryptocurrencies.objects.all()
		return products


class FavoritesView(ListView):
	"""
	Выполняет отображения списка избранных криптовалют по слагу пользователя.
	"""
	template_name = 'cryptocurrencies/favorites.html'
	context_object_name = 'favorites'

	def get_queryset(self):
		queryset = Favorites.objects.filter(slug=self.request.user.username).select_related('cryptocurrencies')
		return queryset

	def post(self, request: HttpRequest, slug):
		if 'product' in request.POST:
			prod_pk = self.request.POST.get('product')
			Favorites.objects.get(pk=prod_pk).delete()
			return redirect('cryptocurrencies:favorites', slug=slug)
