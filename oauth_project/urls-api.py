from django.urls import include, path

from rest_framework import routers

from oauth_project.serializers import MiembroSerializer
from oauth_project.views import PermisoViewSet, UsuarioViewSet, ProyectoViewSet, RolProyectoViewSet, \
   MiembroProyectoViewSet, TipoUserStoryViewSet

router = routers.DefaultRouter()
router.register(r'permisos', PermisoViewSet)
router.register(r'users', UsuarioViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'roles', RolProyectoViewSet)
router.register(r'miembros-proyectos', MiembroProyectoViewSet)
router.register(r'tipos-users-story', TipoUserStoryViewSet)


urlpatterns = [
   path('', include(router.urls)),
]