# Generated by Django 4.2.7 on 2023-12-31 09:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0006_alter_notice_id_alter_notice_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notice",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
