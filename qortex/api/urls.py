from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from .views import AlbumViewSet, ArtistViewSet, SongViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        contact=openapi.Contact(email="i@nikitakolesnik.ru"),
    ),
    public=True,
)
router = DefaultRouter()
router.register(r"artists", ArtistViewSet)
router.register(r"albums", AlbumViewSet)
router.register(r"songs", SongViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger",
    ),
]
