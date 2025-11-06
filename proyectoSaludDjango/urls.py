from gestion_salud import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Página de inicio
    path('', views.index, name='index'),

    # URLs para Pacientes
    path('pacientes/', views.paciente_listar, name='paciente_listar'),
    path('pacientes/crear/', views.paciente_crear, name='paciente_crear'),
    path('pacientes/<int:pk>/actualizar/', views.paciente_actualizar, name='paciente_actualizar'),
    path('pacientes/<int:pk>/eliminar/', views.paciente_eliminar, name='paciente_eliminar'),

    # URLs para Servicios de Salud
    path('servicios/', views.servicio_listar, name='servicio_listar'),
    path('servicios/crear/', views.servicio_crear, name='servicio_crear'),
    path('servicios/<int:pk>/actualizar/', views.servicio_actualizar, name='servicio_actualizar'),
    path('servicios/<int:pk>/eliminar/', views.servicio_eliminar, name='servicio_eliminar'),
]

