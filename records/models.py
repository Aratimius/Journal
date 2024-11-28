from datetime import datetime

from django.db import models

from users.models import User


class Entry(models.Model):
    """Модель записей в дневник"""

    user = models.ForeignKey(
        User, verbose_name="Владелец", on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    is_private = models.BooleanField(default=False, verbose_name="Личное")
    is_purpose = models.BooleanField(default=False, verbose_name="Цель")
    last_viewed = models.BooleanField(default=False)

    PAST = "достигнута"
    PRESENT = "в процессе"
    FUTURE = "в планах"

    STATUS_CHOICES = (
        (PAST, "достигнута"),
        (PRESENT, "в процессе"),
        (FUTURE, "в планах"),
    )

    status = models.CharField(
        max_length=150,
        verbose_name="Статус",
        choices=STATUS_CHOICES,
        blank=True,
        null=True,
    )
    start_time = models.DateTimeField(
        verbose_name="Дата и время начала", default=datetime.now()
    )
    end_time = models.DateTimeField(
        verbose_name="Дата и время окончания", blank=True, null=True
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

        ordering = ("start_time",)


class Objective(models.Model):
    """Модель задач"""

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    time = models.DateTimeField(verbose_name="Начало решения", default=datetime.now())

    is_complete = models.BooleanField(default=False, verbose_name=" ")
    entry = models.ForeignKey(
        Entry,
        on_delete=models.CASCADE,
        verbose_name="Цель",
        related_name="objectives",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

        ordering = (
            "is_complete",
            "time",
        )
