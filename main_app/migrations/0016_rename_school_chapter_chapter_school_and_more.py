# Generated by Django 4.1.2 on 2022-10-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0015_alter_chapter_recharter_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chapter",
            old_name="school",
            new_name="chapter_school",
        ),
        migrations.AddField(
            model_name="school",
            name="can_visit",
            field=models.ManyToManyField(to="main_app.chapter"),
        ),
    ]
