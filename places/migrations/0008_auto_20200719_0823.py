# Generated by Django 3.0.8 on 2020-07-19 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_remove_place_description_long'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long_html',
            new_name='description_long',
        ),
    ]
