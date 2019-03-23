# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 16:36
from __future__ import unicode_literals

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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=90, verbose_name='Nazwa firmy')),
                ('name', models.CharField(max_length=64, verbose_name='Imię')),
                ('surname', models.CharField(max_length=64, verbose_name='Nazwisko')),
                ('street', models.CharField(max_length=350, verbose_name='Ulica')),
                ('house_number', models.IntegerField(verbose_name='Numer domu')),
                ('apartment_number', models.PositiveSmallIntegerField(verbose_name='Numer lokalu')),
                ('zip_code', models.CharField(max_length=6, verbose_name='Kod pocztowy')),
                ('city', models.CharField(max_length=350, verbose_name='Miejscowość')),
                ('user', models.ForeignKey(choices=[(0, 'Sprzedawca'), (1, 'Klient')], on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_list', models.TextField(verbose_name='Lista produktów')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Data wprowadzenia')),
                ('payment_deadline', models.DateTimeField(verbose_name='Termin_platnosci')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sumaryczna cena')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Klient')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nazwa')),
                ('manufacturer', models.CharField(max_length=64, verbose_name='Producent')),
                ('description', models.TextField(verbose_name='Opis')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cena')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Zdjęcie')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='Z_app.Product'),
        ),
    ]