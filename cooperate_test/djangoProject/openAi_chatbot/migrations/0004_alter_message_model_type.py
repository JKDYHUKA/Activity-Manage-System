# Generated by Django 4.2.3 on 2023-07-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("openAi_chatbot", "0003_message_model_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="model_type",
            field=models.CharField(max_length=60),
        ),
    ]
