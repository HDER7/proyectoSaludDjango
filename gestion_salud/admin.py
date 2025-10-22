from django.contrib import admin
from django.utils.html import format_html
from .models import (Pais, Ciudad, OcupacionCIUO, ComunidadEtnica, Etnia,PrestadoraSalud, Discapacidad, VoluntadAnticipada, OposicionDonacion,PacienteNacionalidad, PacienteDiscapacidad,CIE10, Modalidad, CatalogoEnfermedadesHuerfanas, ViaIngreso, CausaMotivo)


# Personalización del sitio de administración
admin.site.site_header = "Sistema de Gestión de Salud"
admin.site.site_title = "SGS Admin"
admin.site.index_title = "Panel de Administración"


# Inlines para relaciones
class PacienteNacionalidadInline(admin.TabularInline):
    model = PacienteNacionalidad
    extra = 1
    verbose_name = "Nacionalidad"
    verbose_name_plural = "Nacionalidades"


class PacienteDiscapacidadInline(admin.TabularInline):
    model = PacienteDiscapacidad
    extra = 0
    verbose_name = "Discapacidad"
    verbose_name_plural = "Discapacidades"


# Registros de administración para catálogos

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['id_pais', 'pais_name']
    search_fields = ['pais_name']
    list_filter = ['pais_name']
    ordering = ['pais_name']

    fieldsets = (
        ('Información del País', {
            'fields': ('pais_name',),
            'description': 'Información básica del país'
        }),
    )


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ['codigo_municipio', 'nombre']
    search_fields = ['nombre', 'codigo_municipio']
    list_filter = ['nombre']
    ordering = ['nombre']

    fieldsets = (
        ('Información de la Ciudad', {
            'fields': ('nombre',),
            'description': 'Datos de la ciudad o municipio'
        }),
    )


@admin.register(OcupacionCIUO)
class OcupacionCIUOAdmin(admin.ModelAdmin):
    list_display = ['codigo_CIUO', 'nombre_ocupacion']
    search_fields = ['nombre_ocupacion', 'codigo_CIUO']
    list_filter = ['nombre_ocupacion']
    ordering = ['nombre_ocupacion']

    fieldsets = (
        ('Clasificación CIUO', {
            'fields': ('nombre_ocupacion',),
            'description': 'Clasificación Internacional Uniforme de Ocupaciones'
        }),
    )


@admin.register(ComunidadEtnica)
class ComunidadEtnicaAdmin(admin.ModelAdmin):
    list_display = ['id_comunidad', 'comunidad']
    search_fields = ['comunidad']
    list_filter = ['comunidad']
    ordering = ['comunidad']

    fieldsets = (
        ('Información de Comunidad', {
            'fields': ('comunidad',),
            'description': 'Código de la comunidad étnica'
        }),
    )


@admin.register(Etnia)
class EtniaAdmin(admin.ModelAdmin):
    list_display = ['id_etnia', 'etnia']
    search_fields = ['etnia']
    list_filter = ['etnia']
    ordering = ['etnia']

    fieldsets = (
        ('Información de Etnia', {
            'fields': ('etnia',),
            'description': 'Código de identificación étnica'
        }),
    )


@admin.register(PrestadoraSalud)
class PrestadoraSaludAdmin(admin.ModelAdmin):
    list_display = ['id_prestadora', 'nombre_prestadora', 'tipo_prestador',
                    'nivel_complejidad', 'municipio', 'departamento']
    search_fields = ['nombre_prestadora', 'nit', 'codigo_habilitacion']
    list_filter = ['tipo_prestador', 'nivel_complejidad', 'departamento', 'municipio']
    ordering = ['nombre_prestadora']

    fieldsets = (
        ('Información Básica', {
            'fields': ('cod_prestadora', 'nombre_prestadora', 'tipo_prestador', 'nivel_complejidad'),
            'description': 'Datos principales de la prestadora'
        }),
        ('Identificación Legal', {
            'fields': ('nit', 'codigo_habilitacion'),
            'description': 'Documentos de identificación y habilitación'
        }),
        ('Ubicación', {
            'fields': ('departamento', 'municipio', 'direccion'),
            'description': 'Información de localización'
        }),
        ('Contacto', {
            'fields': ('contacto',),
            'description': 'Información de contacto'
        }),
    )

    def colored_nivel(self, obj):
        colors = {
            'BAJO': 'green',
            'MEDIO': 'orange',
            'ALTO': 'red'
        }
        color = colors.get(obj.nivel_complejidad, 'gray')
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            obj.nivel_complejidad
        )

    colored_nivel.short_description = 'Nivel de Complejidad'


@admin.register(Discapacidad)
class DiscapacidadAdmin(admin.ModelAdmin):
    list_display = ['id_discapacidad', 'nombre_discapacidad', 'grado',
                    'cod_categoria_discapacidad']
    search_fields = ['nombre_discapacidad', 'cod_categoria_discapacidad']
    list_filter = ['grado', 'cod_categoria_discapacidad']
    ordering = ['nombre_discapacidad']

    fieldsets = (
        ('Información Principal', {
            'fields': ('cod_categoria_discapacidad', 'nombre_discapacidad'),
            'description': 'Datos básicos de la discapacidad'
        }),
        ('Detalles Adicionales', {
            'fields': ('grado', 'observaciones'),
            'description': 'Información complementaria',
            'classes': ('collapse',)
        }),
    )


@admin.register(VoluntadAnticipada)
class VoluntadAnticipadaAdmin(admin.ModelAdmin):
    list_display = ['id_voluntad_anticipada', 'get_paciente_nombre', 'estado_voluntad',
                    'fecha_suscripcion', 'id_prestadora']
    search_fields = ['id_paciente__numero_documento', 'id_paciente__primer_nombre',
                     'id_paciente__primer_apellido']
    list_filter = ['estado_voluntad', 'fecha_suscripcion', 'id_prestadora']
    date_hierarchy = 'fecha_suscripcion'
    ordering = ['-fecha_suscripcion']
    readonly_fields = ['fecha_suscripcion']

    fieldsets = (
        ('Información del Paciente', {
            'fields': ('id_paciente', 'id_prestadora'),
            'description': 'Datos del paciente y prestadora'
        }),
        ('Fechas Importantes', {
            'fields': ('fecha_suscripcion', 'fecha_modificacion', 'fecha_revocacion'),
            'description': 'Control de fechas del documento'
        }),
        ('Contenido del Documento', {
            'fields': ('contenido_documento', 'estado_voluntad', 'firma_paciente'),
            'description': 'Detalles del documento de voluntad anticipada'
        }),
    )

    def get_paciente_nombre(self, obj):
        return f"{obj.id_paciente.primer_nombre} {obj.id_paciente.primer_apellido}"

    get_paciente_nombre.short_description = 'Paciente'


@admin.register(OposicionDonacion)
class OposicionDonacionAdmin(admin.ModelAdmin):
    list_display = ['id_oposicion', 'get_paciente_nombre', 'tiene_oposicion',
                    'fecha_manifestacion', 'testigo']
    search_fields = ['id_paciente__numero_documento', 'id_paciente__primer_nombre',
                     'id_paciente__primer_apellido', 'testigo']
    list_filter = ['tiene_oposicion', 'fecha_manifestacion']
    date_hierarchy = 'fecha_manifestacion'
    ordering = ['-fecha_manifestacion']

    fieldsets = (
        ('Información del Paciente', {
            'fields': ('id_paciente',),
            'description': 'Datos del paciente'
        }),
        ('Decisión de Donación', {
            'fields': ('tiene_oposicion', 'fecha_manifestacion'),
            'description': 'Información sobre la oposición'
        }),
        ('Documentación', {
            'fields': ('documento_soporte', 'testigo', 'registro_notaria'),
            'description': 'Soporte legal y testigos'
        }),
        ('Observaciones', {
            'fields': ('observaciones',),
            'description': 'Notas adicionales',
            'classes': ('collapse',)
        }),
    )

    def get_paciente_nombre(self, obj):
        return f"{obj.id_paciente.primer_nombre} {obj.id_paciente.primer_apellido}"

    get_paciente_nombre.short_description = 'Paciente'


# Registros para modelos intermedios

@admin.register(PacienteNacionalidad)
class PacienteNacionalidadAdmin(admin.ModelAdmin):
    list_display = ['id_paciente_nacionalidad', 'get_paciente_info', 'id_pais']
    search_fields = ['id_paciente__numero_documento', 'id_paciente__primer_nombre',
                     'id_paciente__primer_apellido', 'id_pais__pais_residencia']
    list_filter = ['id_pais']
    raw_id_fields = ['id_paciente']
    autocomplete_fields = ['id_pais']

    fieldsets = (
        ('Relación Paciente-Nacionalidad', {
            'fields': ('id_paciente', 'id_pais'),
            'description': 'Asociación entre paciente y su nacionalidad'
        }),
    )

    def get_paciente_info(self, obj):
        return f"{obj.id_paciente.primer_nombre} {obj.id_paciente.primer_apellido} ({obj.id_paciente.numero_documento})"

    get_paciente_info.short_description = 'Paciente'


@admin.register(PacienteDiscapacidad)
class PacienteDiscapacidadAdmin(admin.ModelAdmin):
    list_display = ['id_paciente_discapacidad', 'get_paciente_info',
                    'id_discapacidad', 'get_grado_discapacidad']
    search_fields = ['id_paciente__numero_documento', 'id_paciente__primer_nombre',
                     'id_paciente__primer_apellido', 'id_discapacidad__nombre_discapacidad']
    list_filter = ['id_discapacidad__grado', 'id_discapacidad']
    raw_id_fields = ['id_paciente']
    autocomplete_fields = ['id_discapacidad']

    fieldsets = (
        ('Relación Paciente-Discapacidad', {
            'fields': ('id_paciente', 'id_discapacidad'),
            'description': 'Asociación entre paciente y sus discapacidades'
        }),
    )

    def get_paciente_info(self, obj):
        return f"{obj.id_paciente.primer_nombre} {obj.id_paciente.primer_apellido}"

    get_paciente_info.short_description = 'Paciente'

    def get_grado_discapacidad(self, obj):
        return obj.id_discapacidad.grado or 'N/A'

    get_grado_discapacidad.short_description = 'Grado'


# Registros para modelos de servicios de salud

@admin.register(CIE10)
class CIE10Admin(admin.ModelAdmin):
    list_display = ['cie_id', 'tipo', 'nombre']
    search_fields = ['nombre', 'tipo']
    list_filter = ['tipo']
    ordering = ['tipo', 'nombre']

    fieldsets = (
        ('Clasificación CIE-10', {
            'fields': ('tipo', 'nombre'),
            'description': 'Clasificación Internacional de Enfermedades'
        }),
    )


@admin.register(Modalidad)
class ModalidadAdmin(admin.ModelAdmin):
    list_display = ['modalidad_id', 'grupo_servicio']
    search_fields = ['grupo_servicio']
    list_filter = ['grupo_servicio']
    ordering = ['grupo_servicio']

    fieldsets = (
        ('Información de Modalidad', {
            'fields': ('grupo_servicio',),
            'description': 'Grupo de servicio de atención'
        }),
    )


@admin.register(CatalogoEnfermedadesHuerfanas)
class CatalogoEnfermedadesHuerfanasAdmin(admin.ModelAdmin):
    list_display = ['id_huerfana', 'nombre', 'tipo']
    search_fields = ['nombre', 'tipo']
    list_filter = ['tipo']
    ordering = ['nombre']

    fieldsets = (
        ('Enfermedad Huérfana', {
            'fields': ('nombre', 'tipo'),
            'description': 'Información de enfermedades raras o huérfanas'
        }),
    )


@admin.register(ViaIngreso)
class ViaIngresoAdmin(admin.ModelAdmin):
    list_display = ['codigo_ingreso', 'nombre_ingreso']
    search_fields = ['nombre_ingreso']
    list_filter = ['nombre_ingreso']
    ordering = ['nombre_ingreso']

    fieldsets = (
        ('Vía de Ingreso', {
            'fields': ('nombre_ingreso',),
            'description': 'Forma de ingreso al sistema de salud'
        }),
    )


@admin.register(CausaMotivo)
class CausaMotivoAdmin(admin.ModelAdmin):
    list_display = ['codigo_motivo', 'nombre_motivo']
    search_fields = ['nombre_motivo']
    list_filter = ['nombre_motivo']
    ordering = ['nombre_motivo']

    fieldsets = (
        ('Motivo de Consulta', {
            'fields': ('nombre_motivo',),
            'description': 'Causa o motivo de la atención'
        }),
    )

