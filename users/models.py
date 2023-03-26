from django.db import models


class News(models.Model):
	title = models.CharField(max_length=200, blank=False, null=False)
	author = models.CharField(max_length=200)
	publishedAt = models.DateTimeField()
	description = models.TextField(blank=False, null=False)
	urlToImage = models.URLField()
	url = models.URLField()

	class Meta:
		ordering = '-publishedAt',
