# Generated by Django 3.2.7 on 2021-09-13 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='canciones',
            old_name='Avatar',
            new_name='AvatarSong',
        ),
    ]
