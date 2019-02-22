# Generated by Django 2.1.7 on 2019-02-20 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('company', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('manager', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=256)),
                ('item_quantity', models.IntegerField()),
                ('item_picture', models.ImageField(blank=True, upload_to='static/main_app/items_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('order_date', models.DateField()),
                ('status', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_name', models.CharField(max_length=256, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('ship_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=256)),
                ('n_m', models.CharField(max_length=256)),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ships', to='main_app.Fleet')),
            ],
        ),
        migrations.CreateModel(
            name='Ship_Type',
            fields=[
                ('type_name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('type_pic', models.ImageField(blank=True, upload_to='static/main_app/items_pics')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ship',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='main_app.Ship_Type'),
        ),
        migrations.AddField(
            model_name='section',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parent', to='main_app.Ship'),
        ),
        migrations.AddField(
            model_name='order',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator', to='main_app.SiteUser'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='main_app.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='main_app.Section'),
        ),
        migrations.AddField(
            model_name='item',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='on_board', to='main_app.Ship'),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('section_name', 'parent')},
        ),
    ]
