# Generated by Django 4.2.2 on 2023-06-18 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="File",
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
                ("name", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to="files/")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("images", "Images"),
                            ("documents", "Documents"),
                            ("videos", "Videos"),
                            ("others", "Others"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "upload_datetime",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
