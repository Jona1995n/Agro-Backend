# Generated by Django 4.2.2 on 2023-06-27 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_review_facility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='facility',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.facility'),
        ),
    ]