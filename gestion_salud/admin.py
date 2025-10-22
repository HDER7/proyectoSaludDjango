from django.contrib import admin
from .models import PrestadoraSalud, VoluntadAnticipada, OposicionDonacion, Paciente, CIE10, CatalogoEnfermedadesHuerfanas, ServicioSalud, CausaMotivo, ViaIngreso, Modalidad, PacienteDiscapacidad, PacienteNacionalidad, Discapacidad, Etnia, ComunidadEtnica, OcupacionCIUO, Ciudad, Pais 
# Register your models here.

class ProductInline(admin.TabularInline):  # También puedes usar admin.StackedInline
    model = CIE10
    extra = 1  # Cuántos formularios vacíos se muestran por defecto
    fields = ('cie_id', 'nombre', 'tipo')
    show_change_link = True  # Agrega el enlace para editar el producto directamente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    # Campos visibles en la lista principal del admin
    list_display = ('id_paciente', 'tipo_documento', 'numero_documento', 'primer_nombre','primer_apellido','fecha_nacimiento','edad','sexo_biologico','fecha_creacion', 'fecha_actualizacion')

    # Campos sobre los que se puede buscar texto
    search_fields = ('primer_nombre','primer_apellido')

    # Filtros laterales por campos
    list_filter = ('fecha_creacion', 'fecha_actualizacion')

    # Orden por defecto al listar
    ordering = ('primer_nombre','primer_apellido',)

    # Número de elementos por página
    list_per_page = 25

    # Mostrar el botón de guardar también arriba del formulario
    save_on_top = True

    # Mostrar acciones (como eliminar) tanto arriba como abajo
    actions_on_top = True
    actions_on_bottom = True

    # Mostrar barra de navegación por fecha (ideal para campos de tipo DateTime)
    date_hierarchy = 'fecha_creacion'

    # Campos que no se pueden modificar
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

    # Agrupación de campos en secciones dentro del formulario
    fieldsets = (
        ('Información básica', {
            'fields': ('id_paciente', 'tipo_documento', 'numero_documento', 'primer_nombre','primer_apellido','fecha_nacimiento','edad','sexo_biologico')
        }),
        ('Tiempos del sistema', {
            'fields': ('fecha_creacion', 'fecha_actualizacion')
        }),
    )