# Generated by Django 4.1.2 on 2022-11-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_alter_userinfo_age"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="book_url",
            new_name="image_url",
        ),
        migrations.AddField(
            model_name="book",
            name="info_url",
            field=models.URLField(blank=True, default="", max_length=2048),
        ),
    ]