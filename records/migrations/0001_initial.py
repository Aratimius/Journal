# Generated by Django 5.1.3 on 2024-11-27 16:16

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "is_private",
                    models.BooleanField(default=False, verbose_name="Личное"),
                ),
                ("is_purpose", models.BooleanField(default=False, verbose_name="Цель")),
                ("last_viewed", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("достигнута", "достигнута"),
                            ("в процессе", "в процессе"),
                            ("в планах", "в планах"),
                        ],
                        max_length=150,
                        null=True,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "start_time",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 11, 27, 19, 16, 37, 723834),
                        verbose_name="Дата и время начала",
                    ),
                ),
                (
                    "end_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата и время окончания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
                "ordering": ("start_time",),
            },
        ),
        migrations.CreateModel(
            name="Objective",
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
                ("title", models.CharField(max_length=200, verbose_name="Название")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "time",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 11, 27, 19, 16, 37, 724193),
                        verbose_name="Начало решения",
                    ),
                ),
                ("is_complete", models.BooleanField(default=False, verbose_name=" ")),
                (
                    "entry",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="objectives",
                        to="records.entry",
                        verbose_name="Цель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задача",
                "verbose_name_plural": "Задачи",
                "ordering": ("is_complete", "time"),
            },
        ),
    ]
