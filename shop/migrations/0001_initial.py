# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-19 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to=b'products/%Y/%m/%d/', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xb0')),
                ('description', models.TextField(blank=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('stock', models.PositiveIntegerField(verbose_name=b'\xd0\x9d\xd0\xb0 \xd1\x81\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5')),
                ('available', models.BooleanField(default=True, verbose_name=b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xb5\xd0\xbd')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x9e\xd0\xb1\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]