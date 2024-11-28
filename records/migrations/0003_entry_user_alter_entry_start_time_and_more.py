# Generated by Django 4.2 on 2024-11-28 01:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("records", "0002_alter_entry_start_time_alter_objective_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AlterField(
            model_name="entry",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 11, 28, 4, 41, 41, 526640),
                verbose_name="Дата и время начала",
            ),
        ),
        migrations.AlterField(
            model_name="objective",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 11, 28, 4, 41, 41, 526938),
                verbose_name="Начало решения",
            ),
        ),
    ]
