from django.urls import re_path
from oauth2_provider import views
from django.urls import path
from .custometokenview import CustomTokenView

app_name = "oauth2_provider"


base_urlpatterns = [
    re_path(r"^authorize/$", views.AuthorizationView.as_view(), name="authorize"),
    re_path("token/", CustomTokenView.as_view(), name="token"),
    re_path(r"^revoke_token/$", views.RevokeTokenView.as_view(), name="revoke-token"),
    re_path(r"^introspect/$", views.IntrospectTokenView.as_view(), name="introspect"),
]

# management_urlpatterns = [
#     # Application management views
#     url(r"^applications/$", views.ApplicationList.as_view(), name="list"),
#     url(r"^applications/register/$", views.ApplicationRegistration.as_view(), name="register"),
#     url(r"^applications/(?P<pk>[\w-]+)/$", views.ApplicationDetail.as_view(), name="detail"),
#     url(r"^applications/(?P<pk>[\w-]+)/delete/$", views.ApplicationDelete.as_view(), name="delete"),
#     url(r"^applications/(?P<pk>[\w-]+)/update/$", views.ApplicationUpdate.as_view(), name="update"),
#     # Token management views
#     url(r"^authorized_tokens/$", views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
#     url(
#         r"^authorized_tokens/(?P<pk>[\w-]+)/delete/$",
#         views.AuthorizedTokenDeleteView.as_view(),
#         name="authorized-token-delete",
#     ),
# ]


urlpatterns = base_urlpatterns
