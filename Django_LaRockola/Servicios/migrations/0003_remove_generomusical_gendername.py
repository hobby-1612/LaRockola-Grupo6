# Generated by Django 3.2.7 on 2021-09-14 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0002_auto_20210913_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generomusical',
            name='GenderName',
        ),
    ]