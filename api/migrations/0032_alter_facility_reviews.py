# Generated by Django 4.2.2 on 2023-06-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_facility_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='reviews',
            field=models.ManyToManyField(to='api.review'),
        ),
    ]
