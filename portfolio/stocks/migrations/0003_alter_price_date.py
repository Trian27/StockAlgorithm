# Generated by Django 4.0.6 on 2023-08-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='date',
            field=models.DateField(),
        ),
    ]
