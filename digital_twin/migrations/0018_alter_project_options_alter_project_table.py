# Generated by Django 5.0.4 on 2024-07-19 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("digital_twin", "0017_alter_project_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"verbose_name_plural": "my_custom_table_name"},
        ),
        migrations.AlterModelTable(
            name="project",
            table=None,
        ),
    ]
