# Generated by Django 4.2.3 on 2023-07-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("openAi_chatbot", "0002_alter_message_id_alter_message_message_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="model_type",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
