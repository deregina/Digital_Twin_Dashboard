# Generated by Django 5.0.4 on 2024-07-19 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("digital_twin", "0014_alter_project_table"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="project_id",
            new_name="id",
        ),
    ]
