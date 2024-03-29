# Generated by Django 4.1.5 on 2023-03-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publishedAt', models.DateTimeField()),
                ('description', models.TextField()),
                ('urlToImage', models.URLField()),
                ('url', models.URLField()),
            ],
        ),
    ]
