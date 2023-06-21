# Generated by Django 4.2.2 on 2023-06-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("noteapp", "0003_alter_tag_options_alter_note_importance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="importance",
            field=models.CharField(
                choices=[
                    ("", "None"),
                    ("low", "1 - Low"),
                    ("medium", "2 - Medium"),
                    ("high", "3 - High"),
                ],
                default="",
                max_length=6,
            ),
        ),
    ]
