import requests

from django.db import transaction
from django.db.models import QuerySet
from django.apps import apps
from django.conf import settings

from zs_utils.api.amocrm import models


__all__ = [
    "AmocrmService",
]


class AmocrmService:
    @classmethod
    def get_amocrm_app_model(
        cls, raise_exception: bool = True
    ) -> type[models.AbstractAmocrmApp] | None:
        model = None
        if settings.AMOCRM_APP_MODEL:
            app_label, model_name = settings.AMOCRM_APP_MODEL.split(".")
            model = apps.get_model(app_label=app_label, model_name=model_name)

        if (not model) and raise_exception:
            raise ValueError("Необходимо задать настройку 'AMOCRM_APP_MODEL'.")

        return model

    @classmethod
    def retrieve_tokens(
        cls,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        refresh_token: str = None,
        code: str = None,
    ) -> dict:
        """
        Получение новых токенов доступа и обновления либос помощью текущего токена обновления,
        либо с помощью одноразового кода.
        """

        assert bool(refresh_token) != bool(
            code
        ), "Необходимо задать либо 'refresh_token', либо 'code'."

        payload = {
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
        }
        if refresh_token:
            payload.update(
                {"grant_type": "refresh_token", "refresh_token": refresh_token}
            )
        else:
            payload.update({"grant_type": "authorization_code", "code": code})

        response = requests.post(
            url=settings.AMOCRM_API_URL + "oauth2/access_token", json=payload
        )
        response.raise_for_status()

        return response.json()

    @classmethod
    @transaction.atomic()
    def retrieve_access_token(cls, app_id: str = None) -> str:
        """
        Получение токена доступа amoCRM
        """

        app_qs: QuerySet[models.AbstractAmocrmApp] = cls.get_amocrm_app_model(
            raise_exception=True
        ).objects.select_for_update()
        if app_id:
            app = app_qs.get(id=app_id)
        else:
            app = app_qs.get(is_default=True)
        if not app.refresh_token:
            raise ValueError("Отсутствует токен обновления AmoCRM.")

        # Получение новых токенов
        response_data = cls.retrieve_tokens(
            client_id=app.client_id,
            client_secret=app.client_secret,
            redirect_uri=app.redirect_uri,
            refresh_token=app.refresh_token,
        )

        # Сохранение нового refresh_token
        app.refresh_token = response_data["refresh_token"]
        app.save(update_fields=["refresh_token"])

        return response_data["access_token"]
