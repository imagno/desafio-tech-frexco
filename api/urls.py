from urllib.parse import urlparse
from rest_framework.routers import DefaultRouter
from api.views import UsuariosViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'usuarios', UsuariosViewSet)

urlpatterns = router.urls
