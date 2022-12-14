# Generated by Django 4.1.2 on 2022-11-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_rename_genre_of_book_genre_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_url",
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="category",
            name="image_url",
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="category",
            name="info_url",
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="genre",
            name="description",
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="genre",
            name="image_url",
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="university",
            name="alumni_mail_address_endpoint",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="university",
            name="student_mail_address_endpoint",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="university",
            name="university",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="location",
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="share_url",
            field=models.URLField(max_length=2048),
        ),
    ]
