# Generated by Django 4.1.2 on 2022-10-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0011_alter_chapter_recharter_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chapter",
            name="recharter_date",
            field=models.DateField(blank=True),
        ),
    ]
