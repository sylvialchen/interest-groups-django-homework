# Generated by Django 4.1.2 on 2022-10-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0012_alter_chapter_recharter_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chapter",
            name="recharter_date",
            field=models.DateField(),
        ),
    ]
