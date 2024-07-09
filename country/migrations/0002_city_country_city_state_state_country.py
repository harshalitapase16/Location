# Generated by Django 4.2.6 on 2024-07-08 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='Country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='country.country'),
        ),
        migrations.AddField(
            model_name='city',
            name='State',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.state'),
        ),
        migrations.AddField(
            model_name='state',
            name='Country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='country.country'),
        ),
    ]