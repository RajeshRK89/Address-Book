from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.views import TokenView
from django.http import HttpResponse


@permission_classes((AllowAny,))
@method_decorator(csrf_exempt, name="dispatch")
class CustomTokenView(APIView):
    """
    Implements an endpoint to provide access tokens

    The endpoint is used in the following flows:
    * Authorization code
    * Password
    * Client credentials
    """

    throttle_recaptcha_scope = "login_api_throttle"

    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    # @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        token_view = TokenView()
        url, headers, body, status = token_view.create_token_response(request)
        response = HttpResponse(content=body, status=status)

        for k, v in headers.items():
            response[k] = v
        return response
