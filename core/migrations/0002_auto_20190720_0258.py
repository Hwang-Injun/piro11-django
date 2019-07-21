# Generated by Django 2.2.3 on 2019-07-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.TextField(default=None, verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]