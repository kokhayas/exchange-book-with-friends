# Generated by Django 4.1.2 on 2022-11-12 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_rename_is_active_userbook_is_sharable_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="genre",
            old_name="genre_of_book",
            new_name="genre",
        ),
    ]