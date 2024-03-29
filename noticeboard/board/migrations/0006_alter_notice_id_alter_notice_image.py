# Generated by Django 4.2.7 on 2023-12-31 09:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0005_emailsubscriber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notice",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid5, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="notice",
            name="image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to="media"
            ),
        ),
    ]
