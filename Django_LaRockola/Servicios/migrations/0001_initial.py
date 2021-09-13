# Generated by Django 3.2.7 on 2021-09-13 01:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('LastName', models.CharField(blank=True, max_length=200, null=True)),
                ('UserName', models.CharField(blank=True, max_length=200, null=True)),
                ('BirthDate', models.DateField(blank=True, default=datetime.datetime, null=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Canciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SongName', models.CharField(blank=True, max_length=200, null=True)),
                ('Gender', models.CharField(blank=True, max_length=200, null=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('Artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.usuario')),
            ],
        ),
    ]
