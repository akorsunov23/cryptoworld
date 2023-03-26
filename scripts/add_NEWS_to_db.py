import os
from datetime import datetime
from users.models import News
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()


def get_news():
	"""
	Запрос актуальных новостей в мире криптовалюты.
	:return: Полученные новости в формате json.
	"""
	client = NewsApiClient(api_key=os.getenv('API_KEY_NEWS'))
	all_articles = client.get_everything(q='crypto', to=datetime.now(), language='ru', sort_by='relevancy')

	for elem in all_articles['articles']:
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
