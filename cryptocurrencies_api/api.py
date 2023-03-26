from rest_framework.request import Request
from rest_framework.mixins import ListModelMixin, \
	CreateModelMixin, \
	UpdateModelMixin, \
	RetrieveModelMixin, \
	DestroyModelMixin
from rest_framework.generics import GenericAPIView
from cryptocurrencies.models import Favorites
from cryptocurrencies_api.serializers import FavoritesSerializer


class FavoritesListView(ListModelMixin, CreateModelMixin, GenericAPIView):
	queryset = Favorites.objects.all()
	serializer_class = FavoritesSerializer

	def get(self, request, *args, **kwargs):
		"""Метод API позволяющий просмотреть все криптовалюты добавленные в избранное."""
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		"""Метод API позволяющий добавить новую запись в БД избранное."""
		return self.create(request, *args, **kwargs)


class FavoritesView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
	serializer_class = FavoritesSerializer
	queryset = Favorites.objects.all()
	lookup_field = 'name_id'

	def get(self, request: Request, *args, **kwargs):
		"""Метод API позволяющий просмотреть информацию о конкретной криптовалюте по символьному коду."""
		return self.retrieve(request, *args, **kwargs)

	def put(self, request: Request, *args, **kwargs):
		"""Метод API позволяющий редактировать информацию о конкретной криптовалюте по символьному коду."""
		return self.update(request, *args, **kwargs)

	def delete(self, request: Request, *args, **kwargs):
		"""Метод API позволяющий удалять криптовалюту по символьному коду."""
		return self.destroy(request, *args, **kwargs)
