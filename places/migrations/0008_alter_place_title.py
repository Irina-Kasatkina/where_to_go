# Generated by Django 4.0.8 on 2022-10-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_image_number_alter_place_long_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='заголовок'),
        ),
    ]
