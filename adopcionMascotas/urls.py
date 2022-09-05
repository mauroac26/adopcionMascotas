from django.contrib import admin
from django.urls import path, include

#from main import views
#from users import views
# from rest_framework import routers

# router = routers.DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
#router.register('mascotas', views.MascotasViewSet)
#router.register('usuario', views.UserViewSet)

urlpatterns = [
  path('main/v1/', include('main.routers')),
  path('admin/', admin.site.urls),
  path('users/', include('users.routers')),
]
