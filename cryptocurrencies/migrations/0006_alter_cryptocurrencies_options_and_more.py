# Generated by Django 4.1.7 on 2023-03-26 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocurrencies', '0005_cryptocurrencies_remove_favorites_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cryptocurrencies',
            options={'ordering': ('-price',)},
        ),
        migrations.AddField(
            model_name='cryptocurrencies',
            name='added',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 3, 26, 11, 18, 5, 297553)),
        ),
        migrations.AlterField(
            model_name='cryptocurrencies',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrencies',
            name='price_percentage_change_24h',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrencies',
            name='volume_24h',
            field=models.CharField(max_length=100),
        ),
    ]