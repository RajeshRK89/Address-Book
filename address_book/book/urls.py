from rest_framework.routers import SimpleRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter
from .views import *

router = SimpleRouter(trailing_slash=False)
extrouter = ExtendedSimpleRouter(trailing_slash=False)

router.register("user", UserViewSet, "user")
router.register("address", AddressViewSet, "address")


extrouter.register(r"user", UserViewSet, basename="user").register(
    r"address",
    AddressViewSet,
    basename="user-address",
    parents_query_lookups=["user"],
)

urlpatterns = router.urls + extrouter.urls
