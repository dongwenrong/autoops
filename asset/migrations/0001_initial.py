# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='外网IP')),
                ('manage_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='管理IP')),
                ('model', models.CharField(max_length=64, null=True, verbose_name='型号')),
                ('cabinet', models.CharField(blank=True, max_length=64, null=True, verbose_name='机柜')),
                ('position', models.CharField(blank=True, max_length=64, null=True, verbose_name='位置')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='序列号')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU')),
                ('memory', models.CharField(blank=True, max_length=64, null=True, verbose_name='内存')),
                ('disk', models.CharField(blank=True, max_length=256, null=True, verbose_name='硬盘')),
                ('port', models.CharField(blank=True, max_length=256, null=True, verbose_name='上联端口')),
                ('ship_time', models.DateField(default='1970-01-01', verbose_name='出厂时间')),
                ('end_time', models.DateField(default='1970-01-01', verbose_name='到保时间')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否启用')),
                ('ps', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '资产管理',
                'db_table': 'asset',
            },
        ),
        migrations.CreateModel(
            name='data_centers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_center_list', models.CharField(max_length=128, null=True, verbose_name='数据中心')),
            ],
            options={
                'verbose_name': '数据中心',
                'verbose_name_plural': '数据中心',
                'db_table': 'data_centers',
            },
        ),
        migrations.CreateModel(
            name='product_lines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_line_list', models.CharField(blank=True, max_length=128, null=True, verbose_name='产品线')),
            ],
            options={
                'verbose_name': '产品线',
                'verbose_name_plural': '产品线',
                'db_table': 'product_lines',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='data_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.data_centers', verbose_name='数据中心'),
        ),
        migrations.AddField(
            model_name='asset',
            name='product_line',
            field=models.ManyToManyField(to='asset.product_lines', verbose_name='产品线'),
        ),
    ]