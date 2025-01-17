# Generated by Django 3.2.5 on 2021-07-11 14:57
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Jobpost",
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
                (
                    "job_title",
                    models.CharField(max_length=60, verbose_name="Job title"),
                ),
                (
                    "job_company_name",
                    models.CharField(max_length=100, verbose_name="Company name"),
                ),
                (
                    "job_description",
                    models.TextField(verbose_name="Describe the position"),
                ),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("PartTime", "Part-time"),
                            ("FullTime", "Full-time"),
                            ("Freelancer", "Freelancer"),
                            ("Internship", "Internship"),
                            ("Other", "Other"),
                        ],
                        max_length=11,
                        verbose_name="Job type",
                    ),
                ),
                (
                    "job_location",
                    models.CharField(max_length=100, verbose_name="Location"),
                ),
                (
                    "job_contact_person",
                    models.CharField(max_length=80, verbose_name="Contact person"),
                ),
                (
                    "job_apply_url",
                    models.URLField(blank=True, verbose_name="Link to job application"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
