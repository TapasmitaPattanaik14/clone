# Generated by Django 5.1.4 on 2024-12-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0007_conversationmemorybuffer"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversationmemorybuffer",
            name="conversation_history",
            field=models.JSONField(blank=True, null=True),
        ),
    ]