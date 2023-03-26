import pytest
from datetime import datetime
from django.urls import reverse
from rest_framework.test import APIClient
from cryptocurrencies.models import Cryptocurrencies


data = {
    "base_name": "test",
    "product_id": "test",
    "price": "test",
    "price_percentage_change_24h": "test",
    "volume_24h": "test",
    "added": datetime.now()
}


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_list_crypt(api_client):
    """Тест, проверяет GET запрос на вывод всех записей из бд, а также валидность возвращаемых данных."""
    url = reverse('cryptocurrencies_api:cryptocurrencies_list')
    response = api_client.get(url)
    print(datetime.now())
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_item_crypt(api_client):
    """Тест, проверяющий POST запрос на добавление записи в БД"""
    global data
    url = reverse('cryptocurrencies_api:cryptocurrencies_list')
    response = api_client.post(url, data, format='json')

    assert Cryptocurrencies.objects.get().base_name == 'test'
    assert Cryptocurrencies.objects.count() == 1
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_item_crypt(api_client):
    """Тест, проверяющий GET запрос на отображение конкретной записи из БД"""
    global data
    url_ = reverse('cryptocurrencies_api:cryptocurrencies_list')
    api_client.post(url_, data, format='json')
    url = f'http://127.0.0.1:8000/api/cryptocurrencies/{data.get("product_id")}/'
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_item_crypt(api_client):
    """Тест, проверяющий PUT запрос на изменение записи в БД"""
    global data
    url_ = reverse('cryptocurrencies_api:cryptocurrencies_list')
    api_client.post(url_, data, format='json')
    url = f'http://127.0.0.1:8000/api/cryptocurrencies/{data.get("product_id")}/'
    new_date = {
        "base_name": "test-new",
        "product_id": "test",
        "price": "test",
        "price_percentage_change_24h": "test",
        "volume_24h": "test",
        "added": datetime.now()
    }
    response = api_client.put(url, new_date)
    assert response.status_code == 200
    assert Cryptocurrencies.objects.get().base_name == 'test-new'


@pytest.mark.django_db
def test_del_item_crypt(api_client):
    """Тест, проверяющий DELETE запрос на удаление записи в БД"""
    global data
    url_ = reverse('cryptocurrencies_api:cryptocurrencies_list')
    api_client.post(url_, data, format='json')
    url = f'http://127.0.0.1:8000/api/cryptocurrencies/{data.get("product_id")}/'

    response = api_client.delete(url, data)
    assert response.status_code == 204
    assert Cryptocurrencies.objects.count() == 0
