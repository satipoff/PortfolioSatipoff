# Generated by Django 4.0.4 on 2022-05-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_postportfolio_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='postportfolio',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/products/%Y/%m/%d'),
        ),
    ]
