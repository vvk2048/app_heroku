# Generated by Django 3.0.7 on 2020-08-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.URLField(max_length=250),
        ),
    ]
