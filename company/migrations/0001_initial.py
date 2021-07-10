# Generated by Django 3.2 on 2021-05-18 11:26
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models

import company.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("logoImage", models.ImageField(null=True, upload_to="images/")),
                ("companyName", models.CharField(max_length=145)),
                ("description", models.TextField()),
                (
                    "websiteURL",
                    models.URLField(
                        blank=True,
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_url",
                                message="Website URL must include https:// or http://",
                                regex="[http]",
                            )
                        ],
                    ),
                ),
                ("relationToDjango", models.TextField()),
                (
                    "phoneNumber",
                    models.CharField(
                        max_length=15, validators=[company.models.Company.only_int]
                    ),
                ),
                ("email", models.EmailField(max_length=100)),
                ("mainContact", models.CharField(max_length=50)),
                ("streetName", models.CharField(max_length=45)),
                ("houseNumber", models.IntegerField()),
                ("postalCode", models.IntegerField()),
                ("region", models.CharField(max_length=45)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]