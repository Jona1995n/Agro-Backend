# Generated by Django 4.2.2 on 2023-06-30 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_facility_reviews_review_facility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='facility',
        ),
    ]
