# Generated by Django 4.1.2 on 2022-11-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_book_book_url_alter_book_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_url",
            field=models.URLField(blank=True, default="", max_length=2048),
        ),
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.CharField(blank=True, default="", max_length=2048),
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.CharField(blank=True, default="", max_length=2048),
        ),
        migrations.AlterField(
            model_name="category",
            name="image_url",
            field=models.URLField(blank=True, default="", max_length=2048),
        ),
        migrations.AlterField(
            model_name="category",
            name="info_url",
            field=models.URLField(blank=True, default="", max_length=2048),
        ),
        migrations.AlterField(
            model_name="genre",
            name="description",
            field=models.CharField(blank=True, default="", max_length=2048),
        ),
        migrations.AlterField(
            model_name="genre",
            name="image_url",
            field=models.URLField(blank=True, default="", max_length=2048),
        ),
        migrations.AlterField(
            model_name="university",
            name="alumni_mail_address_endpoint",
            field=models.CharField(blank=True, default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="university",
            name="student_mail_address_endpoint",
            field=models.CharField(blank=True, default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="age",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="gender_code",
            field=models.CharField(blank=True, default="", max_length=1),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="location",
            field=models.CharField(blank=True, default="", max_length=256),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="pen_name",
            field=models.CharField(blank=True, default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="phone_number",
            field=models.CharField(blank=True, default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="second_email",
            field=models.EmailField(blank=True, default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="share_url",
            field=models.URLField(blank=True, default="", max_length=2048),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="university_email",
            field=models.EmailField(blank=True, default="", max_length=128),
        ),
    ]
