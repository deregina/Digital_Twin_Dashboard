# Generated by Django 5.0.4 on 2024-07-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("digital_twin", "0006_forecasted_data_satellite_forecasted_data_uav_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="location",
            old_name="grids_id",
            new_name="fid",
        ),
        migrations.AddField(
            model_name="location",
            name="metadata",
            field=models.TextField(default="No metadata available"),
        ),
    ]
