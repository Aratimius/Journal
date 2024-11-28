from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="email")
    tg_chat_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="telegram-chat-id",
        help_text="укажите chat id из telegram для получения уведомлений",
    )
    # Для верификации почты ползователя:
    token = models.CharField(
        max_length=100, verbose_name="token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
