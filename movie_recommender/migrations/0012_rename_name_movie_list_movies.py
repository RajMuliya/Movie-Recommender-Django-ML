# Generated by Django 5.1.2 on 2024-10-18 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_recommender', '0011_rename_language_movie_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie_list',
            old_name='name',
            new_name='movies',
        ),
    ]
