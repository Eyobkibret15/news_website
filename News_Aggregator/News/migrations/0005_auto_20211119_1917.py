# Generated by Django 3.2.9 on 2021-11-19 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_auto_20211119_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firstnews',
            options={'verbose_name': 'First News', 'verbose_name_plural': ' First News'},
        ),
        migrations.RemoveField(
            model_name='aljazeera',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='aljazeera',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='art',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='art',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='bbc',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='bbc',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='cnn',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='cnn',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='firstnews',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='firstnews',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='gizmodo',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='gizmodo',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='hackernews',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='hackernews',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='skysport',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='skysport',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='techcrunch',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='techcrunch',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='theguardian',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='theguardian',
            name='comment_link',
        ),
        migrations.RemoveField(
            model_name='tvn24',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='tvn24',
            name='comment_link',
        ),
    ]