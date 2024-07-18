# Generated by Django 5.0.4 on 2024-07-16 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("digital_twin", "0009_alter_project_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experement",
            name="location_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="digital_twin.location"
            ),
        ),
        migrations.AlterField(
            model_name="experement",
            name="project_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="digital_twin.project"
            ),
        ),
        migrations.AlterField(
            model_name="forecasted_data_satellite",
            name="experiment_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="digital_twin.experement",
            ),
        ),
        migrations.AlterField(
            model_name="forecasted_data_satellite",
            name="feature",
            field=models.CharField(
                choices=[
                    ("", "select"),
                    ("NA", "NA"),
                    ("canopy_cover", "canopy_cover"),
                    ("canopy_height", "canopy_height"),
                    ("canopy_volume", "canopy_volume"),
                    ("exg", "exg"),
                    ("ndvi", "ndvi"),
                ],
                default="Unknown",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="forecasted_data_uav",
            name="experiment_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="digital_twin.experement",
            ),
        ),
        migrations.AlterField(
            model_name="forecasted_data_uav",
            name="feature",
            field=models.CharField(
                choices=[
                    ("", "select"),
                    ("NA", "NA"),
                    ("canopy_cover", "canopy_cover"),
                    ("canopy_height", "canopy_height"),
                    ("canopy_volume", "canopy_volume"),
                    ("exg", "exg"),
                    ("ndvi", "ndvi"),
                ],
                default="Unknown",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="acesss",
            field=models.CharField(
                choices=[("public", "public"), ("protected", "protected")],
                default="NA",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="satellite_data",
            name="experiment_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="digital_twin.experement",
            ),
        ),
        migrations.AlterField(
            model_name="satellite_data",
            name="feature",
            field=models.CharField(
                choices=[
                    ("", "select"),
                    ("NA", "NA"),
                    ("canopy_cover", "canopy_cover"),
                    ("canopy_height", "canopy_height"),
                    ("canopy_volume", "canopy_volume"),
                    ("exg", "exg"),
                    ("ndvi", "ndvi"),
                ],
                default="Unknown",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="soil_profile",
            name="location_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="digital_twin.location"
            ),
        ),
        migrations.AlterField(
            model_name="uav_data",
            name="experiment_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="digital_twin.experement",
            ),
        ),
        migrations.AlterField(
            model_name="uav_data",
            name="feature",
            field=models.CharField(
                choices=[
                    ("", "select"),
                    ("NA", "NA"),
                    ("canopy_cover", "canopy_cover"),
                    ("canopy_height", "canopy_height"),
                    ("canopy_volume", "canopy_volume"),
                    ("exg", "exg"),
                    ("ndvi", "ndvi"),
                ],
                default="Unknown",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="weather",
            name="location_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="digital_twin.location"
            ),
        ),
    ]
