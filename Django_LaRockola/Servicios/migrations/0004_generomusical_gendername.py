# Generated by Django 3.2.7 on 2021-09-14 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0003_remove_generomusical_gendername'),
    ]

    operations = [
        migrations.AddField(
            model_name='generomusical',
            name='GenderName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]