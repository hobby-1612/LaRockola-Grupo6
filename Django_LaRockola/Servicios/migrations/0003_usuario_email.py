# Generated by Django 3.2.7 on 2021-09-13 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0002_rename_avatar_canciones_avatarsong'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]