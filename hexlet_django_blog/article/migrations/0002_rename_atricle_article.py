# Generated by Django 5.0.1 on 2024-01-26 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Atricle',
            new_name='Article',
        ),
    ]