# Generated by Django 4.2.2 on 2023-06-26 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]