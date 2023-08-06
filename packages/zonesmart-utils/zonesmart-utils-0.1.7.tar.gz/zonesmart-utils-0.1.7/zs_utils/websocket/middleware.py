import jwt
from urllib.parse import parse_qs
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from django.conf import settings
from django.contrib.auth import get_user_model


class JWTAuthMiddleware(BaseMiddleware):
    @database_sync_to_async
    def get_user(self, user_id: int):
        return get_user_model().objects.get(id=user_id)

    async def __call__(self, scope, receive, send):
        from rest_framework_simplejwt.tokens import UntypedToken

        # Получение токена

        token = None

        if scope["query_string"]:
            query_data = parse_qs(scope["query_string"].decode("utf-8"))
            token = query_data.get("token")
            if token:
                token = token[0]

        if not token:
            for header in scope["headers"]:
                key = header[0].decode("utf-8")
                if key.lower() == "authorization":
                    token = header[1].decode("utf-8")
                    break

        scope["token"] = token

        # Получение пользователя
        if "user" not in scope:
            user = None

            if token:
                try:
                    UntypedToken(token)
                except (InvalidToken, TokenError):
                    # TODO: флаг устаревшего токена
                    pass
                else:
                    decoded_data = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
                    user = await self.get_user(user_id=decoded_data["user_id"])

            scope["user"] = user

        return await super().__call__(scope, receive, send)
