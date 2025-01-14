# Generated by Django 5.0.4 on 2024-07-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("digital_twin", "0002_project_crop_project_project_editors"),
    ]

    operations = [
        migrations.CreateModel(
            name="experements",
            fields=[
                (
                    "experement_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("project_id", models.CharField(default="Unknown", max_length=100)),
                ("location_id", models.CharField(default="Unknown", max_length=100)),
                ("year", models.CharField(default="Unknown", max_length=100)),
                ("planting_date", models.CharField(default="Unknown", max_length=100)),
                ("pix_source_1", models.CharField(default="Unknown", max_length=100)),
                ("pix_rate_1", models.CharField(default="Unknown", max_length=100)),
                ("pix_timing_1", models.CharField(default="Unknown", max_length=100)),
                ("pix_source_2", models.CharField(default="Unknown", max_length=100)),
                ("pix_rate_2", models.CharField(default="Unknown", max_length=100)),
                ("pix_timing_2", models.CharField(default="Unknown", max_length=100)),
                ("pix_source_3", models.CharField(default="Unknown", max_length=100)),
                ("pix_rate_3", models.CharField(default="Unknown", max_length=100)),
                ("pix_timing_3", models.CharField(default="Unknown", max_length=100)),
                ("n_source_1", models.CharField(default="Unknown", max_length=100)),
                ("n_timing_1", models.CharField(default="Unknown", max_length=100)),
                ("n_rate_1", models.CharField(default="Unknown", max_length=100)),
                ("n_source_2", models.CharField(default="Unknown", max_length=100)),
                ("n_timing_2", models.CharField(default="Unknown", max_length=100)),
                ("n_rate_2", models.CharField(default="Unknown", max_length=100)),
                ("n_source_3", models.CharField(default="Unknown", max_length=100)),
                ("n_timing_3", models.CharField(default="Unknown", max_length=100)),
                ("n_rate_3", models.CharField(default="Unknown", max_length=100)),
                ("defoliation_1", models.CharField(default="Unknown", max_length=100)),
                ("defoliation_2", models.CharField(default="Unknown", max_length=100)),
                ("defoliation_3", models.CharField(default="Unknown", max_length=100)),
                ("uav_raw", models.CharField(default="Unknown", max_length=100)),
                ("satellite_raw", models.CharField(default="Unknown", max_length=100)),
                (
                    "uav_orthomosiac_RGB",
                    models.CharField(default="Unknown", max_length=100),
                ),
                (
                    "uav_orthomosiac_MS",
                    models.CharField(default="Unknown", max_length=100),
                ),
                ("uav_dsm", models.CharField(default="Unknown", max_length=100)),
                ("metadata", models.CharField(default="Unknown", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "location_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("year_added", models.CharField(default="Unknown", max_length=100)),
                ("plot_boundary", models.CharField(default="Unknown", max_length=100)),
                ("grids_id", models.CharField(default="Unknown", max_length=100)),
                ("state_id", models.CharField(default="Unknown", max_length=100)),
                ("county_id", models.CharField(default="Unknown", max_length=100)),
                ("latitude", models.CharField(default="Unknown", max_length=100)),
                ("longitude", models.CharField(default="Unknown", max_length=100)),
                ("contact_info", models.CharField(default="Unknown", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="soil_profile",
            fields=[
                (
                    "soil_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("location_id", models.CharField(default="Unknown", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="weather",
            fields=[
                (
                    "weather_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("location_id", models.CharField(default="Unknown", max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name="project",
            old_name="Acesss",
            new_name="acesss",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="Funding_Source",
            new_name="funding_source",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="MetaData",
            new_name="metadata",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="Project_Editors",
            new_name="project_editors",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="Project_ID",
            new_name="project_id",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="Start_year",
            new_name="start_year",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="User_ID",
            new_name="user_id",
        ),
        migrations.RemoveField(
            model_name="project",
            name="Crop",
        ),
        migrations.AddField(
            model_name="project",
            name="crop",
            field=models.CharField(
                choices=[
                    ("", "select"),
                    ("NA", "NA"),
                    ("corn", "corn"),
                    ("cotton", "cotton"),
                    ("rice", "rice"),
                    ("fescue", "fescue"),
                    ("sorgum", "sorgum"),
                ],
                default="NA",
                max_length=50,
            ),
        ),
    ]
