# Generated by Django 4.2.3 on 2024-06-18 05:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("activities_organization", "0003_alter_createactivity_activity_condition"),
    ]

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place_name", models.CharField(max_length=100, unique=True)),
                (
                    "place_type",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(3),
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Unnamed", max_length=100)),
                ("Type", models.CharField(default="none", max_length=30)),
                ("description", models.TextField(default="none", max_length=300)),
                ("cost_in", models.IntegerField(default=0)),
                ("cost_out", models.IntegerField(default=0)),
                ("rest", models.IntegerField(default=0)),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="activities_organization.createactivity",
                        to_field="activity_id",
                    ),
                ),
            ],
        ),
    ]
