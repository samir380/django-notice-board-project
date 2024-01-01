# Generated by Django 4.2.7 on 2023-12-25 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0002_categorytypes_alter_notice_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categorytypes",
            options={"ordering": ("types",), "verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="notice",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="board.categorytypes"
            ),
        ),
    ]
