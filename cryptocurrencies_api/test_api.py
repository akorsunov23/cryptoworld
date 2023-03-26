import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from cryptocurrencies.models import Favorites
from cryptocurrencies_api.serializers import FavoritesSerializer

data = {
    "user_pk": 100,
    "name": "Test",
    "name_id": "Test",
    "price": "5000"
}


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_list_favorites(api_client):
    """Тест, проверяет GET запрос на вывод всех записей из бд, а также валидность возвращаемых данных."""
    url = reverse('cryptocurrencies_api:favorites_list')
    response = api_client.get(url)

    articles = Favorites.objects.all()
    expected_data = FavoritesSerializer(articles, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_add_item_favorites(api_client):
    """Тест, проверяющий POST запрос на добавление записи в БД"""
    global data
    url = reverse('cryptocurrencies_api:favorites_list')
    response = api_client.post(url, data, format='json')
    assert type(data.get('user_pk')) == int
    assert Favorites.objects.get().name == 'Test'
    assert Favorites.objects.count() == 1
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_item_favorites(api_client):
    """Тест, проверяющий GET запрос на отображение конкретной записи из БД"""
    global data
    url_ = reverse('cryptocurrencies_api:favorites_list')
    api_client.post(url_, data, format='json')
    url = f'http://127.0.0.1:8000/api/favorites/detail/{data.get("name_id")}/'
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_item_favorites(api_client):
    """Тест, проверяющий PUT запрос на изменение записи в БД"""
    global data
    url_ = reverse('cryptocurrencies_api:favorites_list')
    api_client.post(url_, data, format='json')
    url = f'http://127.0.0.1:8000/api/favorites/detail/{data.get("name_id")}/'
    new_date = {
        "user_pk": 100,
        "name": "Test_new",
        "name_id": "Test-new",
        "price": "5000"
    }
    response = api_client.put(url, new_date)
    assert response.status_code == 200
    assert Favorites.objects.get().name == 'Test_new'


@pytest.mark.django_db
def test_del_item_favorites(api_client):
    """Тест, проверяющий DELETE запрос на удаление записи в БД"""
    global data
    url_ = reverse('cryptocurrencies_api:favorites_list')
    api_client.post(url_, data, format='json')
    url = f'http://127.0.0.1:8000/api/favorites/detail/{data.get("name_id")}/'

    response = api_client.delete(url, data)
    assert response.status_code == 204
    assert Favorites.objects.count() == 0
