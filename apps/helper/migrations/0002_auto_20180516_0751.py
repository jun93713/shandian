# Generated by Django 2.0.5 on 2018-05-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='isArrived',
            field=models.BooleanField(default=False),
        ),
    ]
