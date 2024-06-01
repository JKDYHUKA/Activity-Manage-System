# Generated by Django 4.2.3 on 2024-06-01 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("activities_organization", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeoption",
            name="activity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="time_options",
                to="activities_organization.createactivity",
                to_field="activity_id",
            ),
        ),
    ]