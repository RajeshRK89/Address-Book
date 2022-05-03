from django.urls import path
from oauth2_provider import views
from django.urls import path
from .custometokenview import CustomTokenView

app_name = "oauth2_provider"


base_urlpatterns = [
    path("authorize", views.AuthorizationView.as_view(), name="authorize"),
    path("token", CustomTokenView.as_view(), name="token"),
    path("revoke_token", views.RevokeTokenView.as_view(), name="revoke-token"),
    path("introspect", views.IntrospectTokenView.as_view(), name="introspect"),
]


urlpatterns = base_urlpatterns
