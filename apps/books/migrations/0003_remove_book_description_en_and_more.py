# Generated by Django 5.1.3 on 2024-11-19 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='book',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='book',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title_uz',
        ),
    ]