from django.contrib.auth import authenticate

from oauth2_provider.oauth2_validators import OAuth2Validator


class OAuth2Validator(OAuth2Validator):
    def validate_user(self, username, password, client, request, *args, **kwargs):
        u = authenticate(username=username, password=password, is_guest=False, is_active=True)
        print(username)
        u = username
        if u is not None and u.is_active:
            request.user = u
            return True
        return False
