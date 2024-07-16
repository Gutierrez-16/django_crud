from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.inicio, name='inicio'),
    path('crear_estudiante/', v.crear_estudiante, name='crear_estudiante'),
    path('editar_estudiante/<int:id>/', v.editar_estudiante, name='editar_estudiante'),
    path('eliminar_estudiante/<int:id>/', v.eliminar_estudiante, name='eliminar_estudiante'),
]
