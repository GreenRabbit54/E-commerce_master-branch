# Generated by Django 3.2 on 2021-05-09 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartphone',
            old_name='accum_volume',
            new_name='accumulator_volume',
        ),
        migrations.RenameField(
            model_name='smartphone',
            old_name='ram',
            new_name='random_access_memory',
        ),
    ]
