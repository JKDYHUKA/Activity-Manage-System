# Generated by Django 4.2.3 on 2023-07-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("openAi_chatbot", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="message",
            name="message",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="message",
            name="role",
            field=models.CharField(max_length=50),
        ),
    ]