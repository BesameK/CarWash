# Generated by Django 3.1.5 on 2021-01-29 16:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carType', models.CharField(max_length=16, verbose_name='Car Make')),
                ('carModel', models.CharField(max_length=16, verbose_name='Car Model')),
                ('carYear', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1886), django.core.validators.MaxValueValidator(2021)], verbose_name='Car Model Year')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='Washer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('percent', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percent from price')),
            ],
            options={
                'verbose_name': 'Washer',
                'verbose_name_plural': 'Washers',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(verbose_name='Order Date/Time')),
                ('end_date', models.DateTimeField(verbose_name='End Date/Time')),
                ('price', models.IntegerField(verbose_name='price')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_wash.car')),
                ('washer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_wash.washer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
