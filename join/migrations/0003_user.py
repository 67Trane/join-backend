# Generated by Django 5.2 on 2025-04-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("join", "0002_rename_email_contact_emailin_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("nameIn", models.CharField(max_length=100)),
            ],
        ),
    ]
