from rest_framework.request import Request
from rest_framework.mixins import ListModelMixin, \
	CreateModelMixin, \
	UpdateModelMixin, \
	RetrieveModelMixin, \
	DestroyModelMixin
from rest_framework.generics import GenericAPIView
from cryptocurrencies.models import Cryptocurrencies
from cryptocurrencies_api.serializers import CryptocurrenciesSerializer
from cryptocurrencies_api.pagination import StandardResultsSetPagination


class CryptocurrenciesListView(ListModelMixin, CreateModelMixin, GenericAPIView):
	queryset = Cryptocurrencies.objects.all()
	serializer_class = CryptocurrenciesSerializer
	pagination_class = StandardResultsSetPagination

	def get(self, request, *args, **kwargs):
		"""Метод API позволяющий просмотреть все криптовалюты из БД."""
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		"""Метод API позволяющий добавить новую запись в БД."""
		return self.create(request, *args, **kwargs)


class CryptocurrenciesView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
	serializer_class = CryptocurrenciesSerializer
	queryset = Cryptocurrencies.objects.all()
	lookup_field = 'product_id'

	def get(self, request: Request, *args, **kwargs):
		"""Метод API позволяющий просмотреть информацию о конкретной криптовалюте по символьному коду."""
		return self.retrieve(request, *args, **kwargs)

	def put(self, request: Request, *args, **kwargs):
		"""Метод API позволяющий редактировать информацию о конкретной криптовалюте по символьному коду."""
		return self.update(request, *args, **kwargs)

	def delete(self, request: Request, *args, **kwargs):
		"""Метод API позволяющий удалять криптовалюту по символьному коду."""
		return self.destroy(request, *args, **kwargs)
