# Generated by Django 3.0.8 on 2020-07-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='point_title',
            field=models.CharField(default='Default', max_length=100, verbose_name='Точка'),
            preserve_default=False,
        ),
    ]
