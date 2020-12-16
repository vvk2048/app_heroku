# Generated by Django 3.0.7 on 2020-10-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_mynews'),
    ]

    operations = [
        migrations.AddField(
            model_name='mynews',
            name='location',
            field=models.CharField(default='hello', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mynews',
            name='source',
            field=models.URLField(max_length=511),
        ),
    ]