# Generated by Django 4.1 on 2023-08-31 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsites', '0002_destination_secondary_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='description',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='title',
            field=models.CharField(max_length=75),
        ),
    ]
