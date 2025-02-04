# Generated by Django 5.1.5 on 2025-02-04 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to='media/products/')),
                ('rating', models.PositiveIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=1)),
                ('shipping_costs', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processor', models.CharField(max_length=250)),
                ('memory', models.CharField(max_length=250)),
                ('brand', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('display', models.CharField(max_length=250)),
                ('storage', models.CharField(max_length=250)),
                ('graphics', models.CharField(max_length=250)),
                ('weight', models.CharField(max_length=250)),
                ('finish', models.CharField(max_length=250)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
