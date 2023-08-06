from model_utils.models import UUIDModel

from django.db import models


__all__ = [
    "AbstractAmocrmApp",
]


class AbstractAmocrmApp(UUIDModel):
    client_id = models.TextField(verbose_name="ID приложения")
    client_secret = models.TextField(verbose_name="Секретный ключ приложения")
    redirect_uri = models.TextField(verbose_name="Redirect URI приложения")

    name = models.CharField(max_length=64, verbose_name="Локальный идентификатор")
    access_token = models.TextField(null=True, verbose_name="Токен доступа")
    refresh_token = models.TextField(
        null=True, verbose_name="Токен для обновления токена доступа"
    )
    is_default = models.BooleanField(
        default=False, verbose_name="Приложение по умолчанию"
    )

    class Meta:
        abstract = True
