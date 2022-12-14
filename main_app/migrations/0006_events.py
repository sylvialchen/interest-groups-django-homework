# Generated by Django 4.1.2 on 2022-10-19 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0005_rename_group_name_school_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Events",
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
                ("date", models.DateField()),
                (
                    "type_of_event",
                    models.CharField(
                        choices=[
                            (1, "Cultural"),
                            (2, "Sisterhood"),
                            (3, "Service"),
                            (4, "Philanthropy"),
                            (5, "RAINN"),
                        ],
                        default=1,
                        max_length=50,
                    ),
                ),
                (
                    "cat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.school",
                    ),
                ),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
