# Generated by Django 4.1.2 on 2022-10-19 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0006_events"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlannedEvent",
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
                ("description", models.TextField(max_length=200)),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
        migrations.AlterField(
            model_name="school",
            name="group_pillars",
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name="Events",
        ),
        migrations.AddField(
            model_name="plannedevent",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main_app.school"
            ),
        ),
    ]