from django.urls import include, path

from oauth_project import viewsabm



































urlpatterns = [
   ##proyecto
   path('crearproyectopost/', viewsabm.crear_proyecto_post, name="crear_proyecto_post"),
   path('crear-us-post/', viewsabm.crear_us_post, name="crear_us_post"),
   path('iniciarproyectoget/<int:id>', viewsabm.iniciar_proyecto_get, name='iniciar_proyecto_get'),
   path('iniciarsprintget/<int:id>/<int:id_proyecto>', viewsabm.iniciar_sprint_get, name='iniciar_sprint_get'),
   path('finalizarsprintget/<int:id>/<int:id_proyecto>', viewsabm.finalizar_sprint_get, name='finalizar_sprint_get'),
   path('cancelarsprintget/<int:id>/<int:id_proyecto>', viewsabm.cancelar_sprint_get, name='cancelar_sprint_get'),
   path('finalizarproyectoget/<int:id>', viewsabm.finalizar_proyecto_get, name='finalizar_proyecto_get'),
   path('cancelarproyectoget/<int:id>', viewsabm.cancelar_proyecto_get, name='cancelar_proyecto_get'),
   path('crearusuario/', viewsabm.crear_nuevo_usuario, name="crear_usuario_post"),

   path('activar_usuario_get/<int:id>', viewsabm.activar_usuario_get, name='activar_usuario_get'),
   path('desactivar_usuario_get/<int:id>', viewsabm.desactivar_usuario_get, name='desactivar_usuario_get'),
   path('reiniciar_password_get/<int:id>', viewsabm.reiniciar_password_get, name='reiniciar_password_get'),

   path('modificar-equipo-proyecto_post/', viewsabm.modificar_equipo_proyecto_post, name='modificar-equipo-proyecto_post'),
   path('modificar-us-proyecto_post/<int:id_proyecto_id>', viewsabm.modificar_us_proyecto_post, name='modificar-us-proyecto_post'),

   #permiso
   path('crearpermisopost/', viewsabm.crear_permiso_post, name="crear_permiso_post"),
   path('eliminarpermisodelete/<int:id>', viewsabm.eliminar_permiso_delete, name='eliminar_permiso_delete'),

   path('eliminar-story-get/<int:id>', viewsabm.eliminar_tipo_story_get, name='eliminar_tipo_story_get'),


   #Roles
   path('crearrolpost/', viewsabm.crear_rol_post, name="crear_rol_post"),
   #path('crearrolpost/<int:id_proyecto_id>', viewsabm.crear_rol_post, name="crear_rol_post"),

   path('importarrolpost/<int:id_proyecto_id>', viewsabm.importar_rol_post, name="importar_rol_post"),
   path('modificar_rol_post/<int:id>/<int:id_proyecto_id>', viewsabm.modificar_rol_post, name='modificar_rol_post'),
   path('actualizar_permisos_rol_post/', viewsabm.actualizar_permisos_rol_post, name='actualizar_permisos_rol_post'),
   path('crear_tipo_user_story/', viewsabm.crear_tipo_user_story, name='crear_tipo_user_story'),
   path('actualizar_tipo_user_story_pos/', viewsabm.actualizar_tipo_user_story_pos, name='actualizar_tipo_user_story_pos'),


   #Miembros
   path('agregar_miembro_proyecto_post/<int:id_proyecto>', viewsabm.agregar_miembro_proyecto_post, name='agregar_miembro_proyecto_post'),
   path('agregar_integrante_proyecto_post/<int:id_proyecto>', viewsabm.agregar_integrante_proyecto_post, name='agregar_integrante_proyecto_post'),
   path('eliminarmiembroproyecto/<int:id_miembro>/<int:id_proyecto>', viewsabm.eliminar_miembro_proyecto_delete, name='eliminar_miembro_proyecto'),
   path('modificarmiembroproyecto/<int:id_miembro>/<int:id_proyecto>', viewsabm.modificar_miembro_proyecto_post, name='modificar_miembro_proyecto_post'),
   path('modificarintegranteproyecto/<int:id_integrante>/<int:id_proyecto>', viewsabm.modificar_integrante_proyecto_post, name='modificar_integrante_proyecto_post'),


   path('crear_tipo_user_story/', viewsabm.crear_tipo_user_story, name='crear_tipo_user_story'),
   path('agregar-sprint-proyecto_post/', viewsabm.view_agregar_sprint_proyecto, name='crear-sprint-post'),
   path('modificar-sprint-proyecto_post/', viewsabm.view_modificar_sprint_proyecto, name='modificar-sprint-post'),
   path('actualizar_tipo_user_story_pos/', viewsabm.actualizar_tipo_user_story_pos, name='actualizar_tipo_user_story_pos'),
   path('registrar-evento-us/', viewsabm.registrar_evento_us, name='registrar_evento_us'),
   path('registrar-evento-us-kanban/', viewsabm.registrar_evento_us_kanban, name='registrar_evento_us_kanban'),


   path('cancelar-us-story-get/<int:id_user_story>', viewsabm.cancelar_user_story, name="cancelar-us-story-get"),
   path('eliminar-integrante-equipo/<int:id_integrante>/<int:id_proyecto>', viewsabm.eliminar_integrante_equipo, name="eliminar-integrante-equipo"),
   path('asignar-sprint-user-story/<int:id_user_story>', viewsabm.asignar_sprint_user_story_post, name="asignar-sprint-user-story_post"),

   path('agregar-integrante-sprint-post/<int:id_sprint>', viewsabm.agregar_integrante_sprint_post, name="agregar_integrante_sprint_post"),
   path('eliminar-integrante-sprint-post/<int:id_sprint>/<int:id_user>', viewsabm.eliminar_integrante_sprint_post, name="eliminar_integrante_sprint_post"),

   path('asignar-us-asignado/<int:id_sprint>', viewsabm.asignar_usuario_us, name="asignar-user-a-us"),
   path('asignar-us-asignado-sprintbacklog/', viewsabm.asignar_usuario_us_sprintbacklog, name="asignar-user-a-us-sprintbackog"),
   path('actualizar_estado_us_post/', viewsabm.actualizar_estado_us_post, name="actualizar_estado_us_post"),

]
