# Generated by Django 4.2.6 on 2024-07-08 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0002_city_country_city_state_state_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='name',
            new_name='s_name',
        ),
    ]
