# Generated by Django 2.1.7 on 2019-02-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20190218_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_picture',
            field=models.ImageField(blank=True, upload_to='static/main_app/items_pics'),
        ),
    ]