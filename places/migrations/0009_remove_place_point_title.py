# Generated by Django 3.0.8 on 2020-07-21 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20200719_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='point_title',
        ),
    ]