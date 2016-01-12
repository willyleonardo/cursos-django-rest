# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcioncurso', models.CharField(max_length=255)),
                ('creditos', models.IntegerField()),
                ('ciclo', models.CharField(max_length=8)),
                ('estadocurso', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipocurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripciontipocurso', models.CharField(max_length=15)),
                ('estadotipo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='tipocurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.tipocurso'),
        ),
    ]