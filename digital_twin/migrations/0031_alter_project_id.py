# Generated by Django 5.0.4 on 2024-07-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("digital_twin", "0030_alter_experement_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]