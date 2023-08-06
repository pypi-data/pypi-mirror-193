from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

User = get_user_model()


class QueryStringAuthentication(BaseAuthentication):
    """Custom authentication with query string token"""

    def authenticate(self, request):
        api_key = request.GET.get("apiKey", None)
        if api_key:
            if api_key == settings.PRONOTE_API_KEY:
                return User(), None
            else:
                raise exceptions.AuthenticationFailed("The apiKey value is wrong.")

        raise exceptions.AuthenticationFailed("Missing authentication.")
