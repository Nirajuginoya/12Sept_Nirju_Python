# Generated by Django 3.0 on 2024-06-06 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studinfo',
            name='created',
        ),
        migrations.RemoveField(
            model_name='studinfo',
            name='updated',
        ),
    ]
