# Generated by Django 4.2.2 on 2023-06-30 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_facility_facility_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='facility_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
