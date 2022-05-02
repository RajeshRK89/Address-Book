from rest_framework.routers import SimpleRouter


from . import views

router = SimpleRouter()
router.register("user", views.UserViewSet, "user")
urlpatterns = api_url_patterns = router.urls
