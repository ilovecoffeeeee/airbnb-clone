# Generated by Django 2.2.5 on 2021-11-28 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='ckeck_in',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='ckeck_out',
            new_name='check_out',
        ),
    ]
