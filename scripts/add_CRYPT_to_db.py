import json
import hmac
import hashlib
import time
import requests
import os
from dotenv import load_dotenv
from cryptocurrencies.models import Cryptocurrencies

load_dotenv()


def get_sign(url_request: str, time_stamp: str) -> str:
	"""
	Генератор зашифрованной подписи. По заданным параметрам генерирует подпись.
	:param url_request: Путь запроса.
	:param time_stamp: Временная метка
	:return: 16-ти значный код для доступа к API.
	"""
	secret_key = os.getenv('API_KEY_SECRET_COINBASE').encode('utf-8')
	request_method = 'GET'
	message = (time_stamp + request_method + url_request + '').encode('utf-8')
	signature = hmac.new(secret_key, message, hashlib.sha256).hexdigest()
	return signature


def search_product():
	"""
	Выполняет запрос API coinbase.com по поиску всех доступных криптовалют.
	Для поиска, в заголовки запроса необходимо передать параметры:
		'Content-Type': 'application/json',
		'CB-ACCESS-KEY': ключ API полученный после регистрации и добавления колюча,
		'CB-ACCESS-SIGN': Зашифрованная подпись, переданная из функции qet_sign(),
		'CB-ACCESS-TIMESTAMP': Временная метка,
	"""
	timestamp = str(int(time.time()))
	url = '/api/v3/brokerage/products'
	url_ = 'https://api.coinbase.com/api/v3/brokerage/products'
	payload = ''
	headers = {
		'Content-Type': 'application/json',
		'CB-ACCESS-KEY': os.getenv('API_KEY_COINBASE'),
		'CB-ACCESS-SIGN': get_sign(url_request=url, time_stamp=timestamp),
		'CB-ACCESS-TIMESTAMP': timestamp,
	}
	a = requests.get(url=url_, headers=headers, params=payload, verify=False)
	data = json.loads(a.text.encode('utf-8'))

	for elem in data['products']:
		Cryptocurrencies.objects.update_or_create(
			base_name=elem['base_name'],
			product_id=elem['product_id'],
			price=elem['price'] if elem['price'] == '' else round(float(elem['price']), 4),
			price_percentage_change_24h=elem['price_percentage_change_24h'] if elem['price_percentage_change_24h'] == '' else
			round(float(elem['price_percentage_change_24h']), 4),
			volume_24h=elem['volume_24h'] if elem['volume_24h'] == '' else round(float(elem['volume_24h']), 4),
		)


def run():
	search_product()
	print('Криптовалюты добавлены в БД')
