from rest_framework.routers import DefaultRouter
from main.views import MascotasViewSet

router = DefaultRouter()

router.register('mascotas', MascotasViewSet)

urlpatterns = router.urls