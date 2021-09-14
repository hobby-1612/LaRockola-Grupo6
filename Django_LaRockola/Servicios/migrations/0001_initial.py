# Generated by Django 3.2.7 on 2021-09-14 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneroMusical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GenderName', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('LastName', models.CharField(blank=True, max_length=200, null=True)),
                ('UserName', models.CharField(blank=True, max_length=200, null=True)),
                ('BirthDay', models.DateField(blank=True, null=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Canciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SongName', models.CharField(blank=True, max_length=200, null=True)),
                ('AvatarSong', models.ImageField(blank=True, null=True, upload_to='')),
                ('ArtistName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.usuario')),
                ('GenderSong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.generomusical')),
            ],
        ),
    ]
