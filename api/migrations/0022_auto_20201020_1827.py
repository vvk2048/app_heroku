# Generated by Django 3.0.7 on 2020-10-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20201020_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynews',
            name='location',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mynews',
            name='source',
            field=models.URLField(max_length=255),
        ),
    ]