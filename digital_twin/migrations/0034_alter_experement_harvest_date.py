# Generated by Django 5.0.4 on 2024-07-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("digital_twin", "0033_location_owner_alter_project_start_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experement",
            name="harvest_date",
            field=models.DateField(default="Unknown"),
        ),
    ]