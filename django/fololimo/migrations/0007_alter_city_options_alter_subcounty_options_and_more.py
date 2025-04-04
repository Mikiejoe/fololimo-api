# Generated by Django 5.1.1 on 2024-10-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fololimo', '0006_alter_client_type_farm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='subcounty',
            options={'verbose_name_plural': 'Sub Counties'},
        ),
        migrations.AlterModelOptions(
            name='weather',
            options={'verbose_name_plural': 'Weather'},
        ),
        migrations.AddField(
            model_name='weather',
            name='humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='max_temp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='min_temp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='pressure',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
