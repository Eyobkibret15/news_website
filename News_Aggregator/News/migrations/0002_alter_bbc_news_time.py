# Generated by Django 3.2.9 on 2021-11-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbc',
            name='news_time',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
