# Generated by Django 4.2.2 on 2023-06-27 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_review_facility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='facility',
        ),
    ]
