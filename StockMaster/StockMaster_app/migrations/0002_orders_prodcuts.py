# Generated by Django 2.2.4 on 2023-07-21 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StockMaster_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodcuts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=255)),
                ('p_barcode', models.IntegerField()),
                ('expire_date', models.DateTimeField()),
                ('cost', models.FloatField()),
                ('qty', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='StockMaster_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_price', models.FloatField()),
                ('qty_sell', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='StockMaster_app.Prodcuts')),
            ],
        ),
    ]