# Generated by Django 4.0.8 on 2022-10-14 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_image_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='позиция'),
        ),
    ]