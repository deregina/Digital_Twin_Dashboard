# Generated by Django 5.0.4 on 2024-07-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("digital_twin", "0012_alter_project_project_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="project_id",
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
    ]