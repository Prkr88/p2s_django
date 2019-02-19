# Generated by Django 2.1.7 on 2019-02-18 19:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190218_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship_Type',
            fields=[
                ('type_name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('type_pic', models.ImageField(blank=True, upload_to='static/main_app/items_pics')),
            ],
        ),
        migrations.AddField(
            model_name='ship',
            name='n_m',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ship',
            name='type',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.PROTECT, related_name='type', to='main_app.Ship_Type'),
            preserve_default=False,
        ),
    ]