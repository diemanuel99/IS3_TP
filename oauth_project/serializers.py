from rest_framework import serializers

from oauth_project.models.modelos import Permiso, Proyecto, RolProyecto, Miembro, TipoUserStory
from django.contrib.auth.models import User


class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ('id', 'descripcion')


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['id', 'nombre_proyecto', 'scrum_master']

class RolProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RolProyecto
        fields = ['id', 'descripcion', 'proyecto']

class MiembroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miembro
        fields = ['id', 'rol_en_Proyecto_id', 'cod_user_id']

class TipoUserStorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoUserStory
        fields = ['id', 'descripcion', 'estados']