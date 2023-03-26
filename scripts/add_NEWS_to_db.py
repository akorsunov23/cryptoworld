import json
import requests
import os
from datetime import datetime
from users.models import News
from dotenv import load_dotenv

load_dotenv()


def get_news():
	"""
	Запрос актуальных новостей в мире криптовалюты.
	:return: Полученные новости в формате json.
	"""
	now_date = datetime.now().strftime('%Y-%m-%d')
	url = ('https://newsapi.org/v2/everything?q=cryptocurrencies&from={now_date}&sortBy=popularity&apiKey={key}'.format(
		now_date=now_date,
		key=os.getenv('API_KEY_NEWS')))

	response = requests.get(url)
	data = json.loads(response.text.encode('utf-8'))

	for elem in data['articles']:
		print(elem['author'])
		News.objects.update_or_create(
			title=elem['title'],
			author=elem['author'],
			publishedAt=elem['publishedAt'],
			description=elem['description'],
			urlToImage=elem['urlToImage'],
			url=elem['url'],
		)


def run():
	get_news()
	print('Новости добавлены в БД')
