# Generated by Django 4.0 on 2021-12-18 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='contact',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
