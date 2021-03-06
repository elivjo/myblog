# Generated by Django 2.2 on 2021-01-18 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0005_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-post_date']},
        ),
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_report', models.TextField(help_text='Enter comment about post here.', max_length=1000)),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('blog_report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.Post')),
            ],
            options={
                'ordering': ['-report_date'],
            },
        ),
    ]