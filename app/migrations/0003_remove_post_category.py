# Generated by Django 4.0.4 on 2022-05-27 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_postportfolio_urltoproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]