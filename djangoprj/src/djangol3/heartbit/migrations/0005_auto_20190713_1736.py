# Generated by Django 2.2.1 on 2019-07-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartbit', '0004_auto_20190712_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostic',
            name='diag_result',
            field=models.FloatField(default=0.0),
        ),
    ]
