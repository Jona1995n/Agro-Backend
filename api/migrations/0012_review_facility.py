# Generated by Django 4.2.2 on 2023-06-30 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_review_facility'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='facility',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.facility'),
        ),
    ]