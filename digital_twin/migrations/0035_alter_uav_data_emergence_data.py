# Generated by Django 5.0.4 on 2024-07-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("digital_twin", "0034_alter_experement_harvest_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uav_data",
            name="emergence_data",
            field=models.DateField(default="Unknown"),
        ),
    ]