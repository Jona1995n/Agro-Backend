# Generated by Django 4.2.2 on 2023-07-20 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_alter_facility_lat_alter_facility_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
