# Generated by Django 2.2 on 2020-12-12 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogauthor',
            options={'ordering': ['author']},
        ),
        migrations.RenameField(
            model_name='blogauthor',
            old_name='bloger',
            new_name='author',
        ),
    ]
