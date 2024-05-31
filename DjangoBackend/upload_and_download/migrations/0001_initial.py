# Generated by Django 4.2.13 on 2024-05-30 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "activities_organization",
            "0002_notice_remove_creatactivity_activity_admin_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="FileInfo",
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
                ("file_name", models.CharField(max_length=500)),
                ("file_size", models.DecimalField(decimal_places=0, max_digits=10)),
                ("file_path", models.CharField(max_length=500)),
                (
                    "active",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="activities_organization.creatactivity",
                    ),
                ),
            ],
        ),
    ]
