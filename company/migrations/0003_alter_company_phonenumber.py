# Generated by Django 3.2.2 on 2021-05-07 13:23
import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0002_auto_20210506_1337"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="phoneNumber",
            field=models.CharField(
                max_length=17,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Det er forkert", regex="^\\+?1?\\d{9,15}$"
                    )
                ],
            ),
        ),
    ]