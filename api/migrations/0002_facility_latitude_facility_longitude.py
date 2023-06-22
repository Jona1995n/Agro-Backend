# Generated by Django 4.2.2 on 2023-06-22 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='latitude',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='facility',
            name='longitude',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
        ),
    ]