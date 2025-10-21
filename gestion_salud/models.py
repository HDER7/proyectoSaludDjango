# LIBRERIAS: 

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Modelos basicos

# =================================
# Modelo para gestionar paises ====
# =================================

class Pais(models.Model):
    """
    Representa un país.

    Campos principales:
    - id_pais: clave primaria autoincremental.
    - pais_name: nombre del país.

    Este modelo se usa como catálogo para referenciar la nacionalidad
    o el país asociado a otros registros (por ejemplo, pacientes).
    """
    id_pais = models.AutoField(primary_key=True)
    pais_name = models.CharField(max_length=200, verbose_name="Nombre del pais")

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ['pais_nombre']
        db_table = 'pais'

    def __str__(self):
        return self.pais_name

# =================================
# Modelo para gestionar ciudades ==
# =================================

class Ciudad(models.Model):
    """
    Representa una ciudad o municipio.

    Campos principales:
    - codigo_municipio: clave primaria autoincremental.
    - nombre: nombre de la ciudad.

    Utilizado como catálogo para relacionar direcciones o residencia de
    pacientes y prestadoras de salud.
    """
    codigo_municipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la ciudad")

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ['nombre']
        db_table = 'ciudad'

    def __str__(self):
        return self.nombre

# ========================================================================
# Modelo de Clasificación internacional uniforme de ocupaciones (CIUO). ==
# ========================================================================

class OcupacionCIUO(models.Model):
    """
    Campos principales:
    - codigo_CIUO: clave primaria autoincremental.
    - nombre_ocupacion: descripción de la ocupación.

    Se utiliza para normalizar la ocupación laboral de pacientes.
    """
    codigo_CIUO = models.AutoField(primary_key=True)
    nombre_ocupacion = models.CharField(max_length=200, verbose_name="Nombre de la ocupacion")

    class Meta:
        verbose_name = "Ocupacion CIUO"
        verbose_name_plural = "Ocupaciones CIUO"
        ordering = ['nombre_ocupacion']
        db_table = 'ocupacion_ciuo'


# ===============================================
# Modelo para gestionar comunidades de etnicas == 
# ===============================================

class ComunidadEtnica(models.Model):
    """
    Representa un código de comunidad étnica.

    Campos principales:
    - id_comunidad: clave primaria autoincremental.
    - comunidad: código de la comunidad étnica.

    Sirve como catálogo para clasificar la pertenencia étnica de pacientes.
    """
    id_comunidad =  models.AutoField(primary_key=True)
    comunidad = models.CharField(max_length=3, verbose_name="Codigo de la comunidad")

    class Meta:
        verbose_name = "Comunidad Etnica"
        verbose_name_plural = "Comunidades Etnicas"
        ordering = ['comunidad']
        db_table = 'comunidad_etnica'

# ================================
# Modelo para gestionar etnias ===
# ================================

class Etnia(models.Model):
    """
    Representa una etnia.

    Campos principales:
    - id_etnia: clave primaria autoincremental.
    - etnia: código o nombre corto de la etnia.

    Usado como referencia en la ficha de paciente para identificar
    la etnia declarada.
    """
    id_etnia = models.AutoField(primary_key=True)
    etnia = models.CharField(max_length=2, verbose_name="Codigo de la etnia")

    class Meta:
        verbose_name = "Etnia"
        verbose_name_plural = "Etnias"
        ordering = ['etnia']
        db_table = 'etnia'

    def __str__(self):
        return self.etnia

# =============================================
# Modelo para gestionar prestadoras de salud ==
# =============================================


class PrestadoraSalud(models.Model):
    """



    Representa una entidad proveedora de servicios de salud (EPS, IPS u otras).

    Campos relevantes:
    - id_prestadora: clave primaria.
    - cod_prestadora, tipo_prestador, nombre_prestadora: identificación y tipo.
    - nivel_complejidad, nit, codigo_habilitacion: datos administrativos.
    - municipio, departamento, direccion, contacto: ubicación y contacto.

    Este modelo se relaciona con pacientes y servicios para indicar
    la prestadora responsable de la atención.
    """
    id_prestadora = models.AutoField(primary_key=True)
    cod_prestadora = models.IntegerField(verbose_name="Código de prestadora")
    tipo_prestador = models.CharField(max_length=100, verbose_name="Tipo de prestador")
    nombre_prestadora = models.CharField(max_length=100, verbose_name="Nombre de la prestadora")
    nivel_complejidad = models.CharField(max_length=20, verbose_name="Nivel de complejidad")
    nit = models.CharField(max_length=13, verbose_name="NIT")
    codigo_habilitacion = models.CharField(max_length=20, verbose_name="Código de habilitación")
    municipio = models.CharField(max_length=50, verbose_name="Municipio")
    departamento = models.CharField(max_length=50, verbose_name="Departamento")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    contacto = models.CharField(max_length=50, verbose_name="Contacto")

    class Meta:
        verbose_name = "Prestadora de Salud"
        verbose_name_plural = "Prestadoras de Salud"
        ordering = ['nombre_prestadora']
        db_table = 'prestadora_salud'

    def __str__(self):
        return f"{self.nombre_prestadora} - {self.tipo_prestador}"


# =============================================
# Modelo para gestionar tipos de discapacidad =
# =============================================

class Discapacidad(models.Model):
    """

    Define los tipos o categorías de discapacidad.

    Campos principales:
    - id_discapacidad: clave primaria.
    - cod_categoria_discapacidad: código de la categoría.
    - nombre_discapacidad: descripción del tipo de discapacidad.
    - observaciones, grado: campos opcionales con detalles adicionales.

    Se usa como catálogo para registrar discapacidades relacionadas a pacientes.
    """
    id_discapacidad = models.AutoField(primary_key=True)
    cod_categoria_discapacidad = models.CharField(max_length=50, verbose_name="Código de categoría")
    nombre_discapacidad = models.CharField(max_length=200, verbose_name="Nombre de la discapacidad")
    observaciones = models.CharField(max_length=200, blank=True, null=True, verbose_name="Observaciones")
    grado = models.CharField(max_length=50, blank=True, null=True, verbose_name="Grado")

    class Meta:
        verbose_name = "Discapacidad"
        verbose_name_plural = "Discapacidades"
        ordering = ['nombre_discapacidad']
        db_table = 'discapacidad'

    def __str__(self):
        return f"{self.nombre_discapacidad} - {self.grado or 'Sin grado'}"


# ===============================================
# Modelo para gestionar voluntades anticipadas ==
# ===============================================
class VoluntadAnticipada(models.Model):
    """



    Registro de voluntades anticipadas de un paciente.

    Campos clave:
    - id_voluntad_anticipada: clave primaria.
    - id_paciente: referencia al paciente que suscribe la voluntad.
    - id_prestadora: prestadora asociada al documento.
    - fecha_suscripcion, fecha_modificacion, fecha_revocacion: timestamps.
    - contenido_documento: texto breve del documento.
    - estado_voluntad: estado actual (activa, revocada, modificada).
    - firma_paciente: representación de la firma o identificador.

    Este modelo permite auditar y relacionar la voluntad anticipada con
    la ficha del paciente.
    """
    ESTADOS_CHOICES = [
        ('ACTIVA', 'Activa'),
        ('REVOCADA', 'Revocada'),
        ('MODIFICADA', 'Modificada'),
    ]

    id_voluntad_anticipada = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE,
                                    related_name='voluntades_anticipadas',
                                    verbose_name="Paciente")
    id_prestadora = models.ForeignKey(PrestadoraSalud, on_delete=models.PROTECT,
                                      verbose_name="Prestadora")
    fecha_suscripcion = models.DateTimeField(verbose_name="Fecha de suscripción")
    fecha_modificacion = models.DateTimeField(blank=True, null=True,
                                              verbose_name="Fecha de modificación")
    fecha_revocacion = models.DateTimeField(blank=True, null=True,
                                            verbose_name="Fecha de revocación")
    contenido_documento = models.CharField(max_length=500, verbose_name="Contenido del documento")
    estado_voluntad = models.CharField(max_length=10, choices=ESTADOS_CHOICES,
                                       default='ACTIVA', verbose_name="Estado de la voluntad")
    firma_paciente = models.CharField(max_length=100, verbose_name="Firma del paciente")

    class Meta:
        verbose_name = "Voluntad Anticipada"
        verbose_name_plural = "Voluntades Anticipadas"
        ordering = ['-fecha_suscripcion']
        db_table = 'voluntad_anticipada'

    def __str__(self):
        return f"Voluntad de {self.id_paciente} - {self.estado_voluntad}"

# ===========================================================
#   Modelo para gestionar oposición a donación de órganos ===
# ===========================================================

class OposicionDonacion(models.Model):
    """

    Indica si un paciente se opone a la donación de sus órganos.

    Campos principales:
    - id_oposicion: clave primaria.
    - id_paciente: paciente que manifiesta la oposición.
    - tiene_oposicion: booleano que indica la oposición.
    - fecha_manifestacion: fecha de la declaración.
    - documento_soporte, observaciones, testigo, registro_notaria: campos opcionales
      para enlace a pruebas o anotaciones legales.

    Se relaciona con la ficha del paciente y puede usarse para decisiones
    clínicas y legales sobre donación.
    """

    id_oposicion = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(
        'Paciente',
        on_delete=models.CASCADE,
        related_name='oposiciones_donacion',
        verbose_name="Paciente",
    )
    tiene_oposicion = models.BooleanField(default=False, verbose_name="Tiene oposición")
    fecha_manifestacion = models.DateTimeField(verbose_name="Fecha de manifestación")
    documento_soporte = models.BinaryField(blank=True, null=True, verbose_name="Documento soporte")
    observaciones = models.CharField(max_length=200, blank=True, null=True,
                                     verbose_name="Observaciones")
    testigo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Testigo")
    registro_notaria = models.CharField(max_length=200, blank=True, null=True,
                                        verbose_name="Registro de notaría")

    class Meta:
        verbose_name = "Oposición a Donación"
        verbose_name_plural = "Oposiciones a Donación"
        ordering = ['-fecha_manifestacion']
        db_table = 'oposicion_donacion'

    def __str__(self):
        estado = "Con oposición" if self.tiene_oposicion else "Sin oposición"
        return f"{self.id_paciente} - {estado}"


# ================== MODELOS PRINCIPALES =====================

# ============================================================
# Modelo principal para gestionar información de pacientes ===
# ============================================================

class Paciente(models.Model):
    """

    def: Información demográfica y administrativa de un paciente.

    Campos destacados y relaciones:
    - id_paciente: clave primaria.
    - Relaciones con catálogos: nacionalidad, país, ciudad, ocupación,
      comunidad étnica, etnia, prestadora, voluntades y oposición a donación.
    - Datos personales: tipo y número de documento, nombres, apellidos,
      fecha de nacimiento, edad, sexo biológico e identidad de género.
    - fechas de auditoría: fecha_creacion y fecha_actualizacion.

    Reglas importantes (no implementadas explícitamente aquí): el número de
    documento es único. Las relaciones permiten construir la ficha completa
    del paciente para su atención en el sistema de salud.
    """

    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ('RC', 'Registro Civil'),
    ]

    SEXO_BIOLOGICO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('I', 'Intersexual'),
    ]

    id_paciente = models.AutoField(primary_key=True)

    # Relaciones con catálogos
    id_nacionalidad = models.ForeignKey('PacienteNacionalidad', on_delete=models.PROTECT,
                                        related_name='pacientes', verbose_name="Nacionalidad")
    id_voluntad_anticipada = models.ForeignKey(VoluntadAnticipada, on_delete=models.SET_NULL,
                                               blank=True, null=True,
                                               verbose_name="Voluntad anticipada")
    id_paciente_pais = models.ForeignKey(Pais, on_delete=models.PROTECT,
                                         verbose_name="País")
    codigo_municipio = models.ForeignKey(Ciudad, on_delete=models.PROTECT,
                                         verbose_name="Municipio")
    codigo_CIUO = models.ForeignKey(OcupacionCIUO, on_delete=models.PROTECT,
                                    verbose_name="Ocupación")
    id_comunidad = models.ForeignKey(ComunidadEtnica, on_delete=models.PROTECT,
                                     verbose_name="Comunidad étnica")
    id_etnia = models.ForeignKey(Etnia, on_delete=models.PROTECT,
                                 verbose_name="Etnia")
    id_prestadora = models.ForeignKey(PrestadoraSalud, on_delete=models.PROTECT,
                                      verbose_name="Prestadora de salud")
    id_oposicion = models.ForeignKey(OposicionDonacion, on_delete=models.SET_NULL,
                                     blank=True, null=True,
                                     verbose_name="Oposición a donación")
    id_paciente_discapacidad = models.ForeignKey('PacienteDiscapacidad',
                                                 on_delete=models.SET_NULL,
                                                 blank=True, null=True,
                                                 verbose_name="Discapacidades")

    # Datos personales
    tipo_documento = models.CharField(max_length=5, choices=TIPO_DOCUMENTO_CHOICES,
                                      verbose_name="Tipo de documento")
    numero_documento = models.CharField(max_length=15, unique=True,
                                        verbose_name="Número de documento")
    primer_nombre = models.CharField(max_length=30, verbose_name="Primer nombre")
    segundo_nombre = models.CharField(max_length=30, blank=True, null=True,
                                      verbose_name="Segundo nombre")
    primer_apellido = models.CharField(max_length=30, verbose_name="Primer apellido")
    segundo_apellido = models.CharField(max_length=30, blank=True, null=True,
                                        verbose_name="Segundo apellido")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    edad = models.IntegerField(verbose_name="Edad")
    sexo_biologico = models.CharField(max_length=10, choices=SEXO_BIOLOGICO_CHOICES,
                                      verbose_name="Sexo biológico")
    identidad_genero = models.CharField(max_length=50, blank=True, null=True,
                                        verbose_name="Identidad de género")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['primer_apellido', 'primer_nombre']
        db_table = 'paciente'

    def __str__(self):
        nombre_completo = f"{self.primer_nombre} {self.segundo_nombre or ''} {self.primer_apellido} {self.segundo_apellido or ''}"
        return f"{nombre_completo.strip()} - {self.numero_documento}"


# =================================================================
#  Modelo intermedio para gestionar nacionalidades de pacientes ===
# =================================================================

class PacienteNacionalidad(models.Model):
    """

   

    Def: Tabla intermedia para asociar uno o varios países (nacionalidades)
    a un paciente.

    Campos:
    - id_paciente_nacionalidad: clave primaria.
    - id_paciente: referencia al paciente.
    - id_pais: referencia al país (nacionalidad).

    La restricción unique_together evita duplicados de la misma nacionalidad
    para un paciente.
    """
    id_paciente_nacionalidad = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,
                                    related_name='nacionalidades',
                                    verbose_name="Paciente")
    id_pais = models.ForeignKey(Pais, on_delete=models.PROTECT,
                                verbose_name="País")

    class Meta:
        verbose_name = "Nacionalidad del Paciente"
        verbose_name_plural = "Nacionalidades de Pacientes"
        ordering = ['id_paciente', 'id_pais']
        db_table = 'paciente_nacionalidad'
        unique_together = [['id_paciente', 'id_pais']]

    def __str__(self):
        return f"{self.id_paciente} - {self.id_pais}"

# =================================================================
# Modelo intermedio para gestionar discapacidades de pacientes ====
# =================================================================

class PacienteDiscapacidad(models.Model):
    """
    Def: Tabla intermedia que relaciona pacientes con las discapacidades
    que presentan.

    Campos:
    - id_paciente_discapacidad: clave primaria.
    - id_paciente: paciente relacionado.
    - id_discapacidad: discapacidad referenciada.

    La combinación paciente-discapacidad es única para evitar duplicados.
    """
    id_paciente_discapacidad = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,
                                    related_name='discapacidades',
                                    verbose_name="Paciente")
    id_discapacidad = models.ForeignKey(Discapacidad, on_delete=models.PROTECT,
                                        verbose_name="Discapacidad")

    class Meta:
        verbose_name = "Discapacidad del Paciente"
        verbose_name_plural = "Discapacidades de Pacientes"
        ordering = ['id_paciente', 'id_discapacidad']
        db_table = 'paciente_discapacidad'
        unique_together = [['id_paciente', 'id_discapacidad']]

    def __str__(self):
        return f"{self.id_paciente} - {self.id_discapacidad}"

# =============================================
# Modelos de servicios de salud ===============
# =============================================

class CIE10(models.Model):
    """
    Clasificación Internacional de Enfermedades

    Def: Catálogo CIE-10 de diagnósticos médicos.

    Campos:
    - cie_id: clave primaria.
    - nombre: descripción del diagnóstico.
    - tipo: código corto o categoría del diagnóstico.

    Utilizado para asignar diagnósticos a servicios y registros clínicos.
    """
    cie_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    tipo = models.CharField(max_length=2, verbose_name="Tipo")

    class Meta:
        verbose_name = "CIE-10"
        verbose_name_plural = "CIE-10"
        ordering = ['nombre']
        db_table = 'cie10'

    def __str__(self):
        return f"{self.tipo} - {self.nombre}"

# =============================================
# Modelo para modalidades de atención =========
# =============================================

class Modalidad(models.Model):
    """
    Modalidad o grupo de servicio para clasificar el tipo de atención.

    Campos:
    - modalidad_id: clave primaria.
    - grupo_servicio: código del grupo de servicio.

    Se usa en los encuentros o servicios para indicar la modalidad.
    """
    modalidad_id = models.AutoField(primary_key=True)
    grupo_servicio = models.CharField(max_length=2, verbose_name="Grupo de servicio")

    class Meta:
        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"
        ordering = ['grupo_servicio']
        db_table = 'modalidad'

    def __str__(self):
        return self.grupo_servicio

# =============================================
# Catálogo de enfermedades huérfanas (raras) ==
# =============================================

class CatalogoEnfermedadesHuerfanas(models.Model):
    """
    Catálogo de enfermedades huérfanas (raras).

    Campos:
    - id_huerfana: clave primaria.
    - nombre: nombre de la enfermedad.
    - tipo: categoría o código asociado.

    Permite marcar si un diagnóstico corresponde a una enfermedad rara
    en servicios clínicos.
    """
    id_huerfana = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    tipo = models.CharField(max_length=2, verbose_name="Tipo")

    class Meta:
        verbose_name = "Enfermedad Huérfana"
        verbose_name_plural = "Enfermedades Huérfanas"
        ordering = ['nombre']
        db_table = 'catalogo_enfermedades_huerfanas'

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

# =============================================
# = Vías de ingreso al sistema de salud =======
# =============================================

class ViaIngreso(models.Model):
    """
    Representa una vía de ingreso o motivo por el cual un paciente
    accede al servicio (por ejemplo, urgencia, cita programada, etc.).

    Campos:
    - codigo_ingreso: clave primaria.
    - nombre_ingreso: descripción de la vía de ingreso.
    """
    codigo_ingreso = models.AutoField(primary_key=True)
    nombre_ingreso = models.CharField(max_length=50, verbose_name="Nombre del ingreso")

    class Meta:
        verbose_name = "Vía de Ingreso"
        verbose_name_plural = "Vías de Ingreso"
        ordering = ['nombre_ingreso']
        db_table = 'via_ingreso'

    def __str__(self):
        return self.nombre_ingreso

# ===============================
# Causas o motivos de consulta ==
# ===============================

class CausaMotivo(models.Model):
    """
    Catálogo de causas o motivos de consulta.

    Campos:
    - codigo_motivo: clave primaria.
    - nombre_motivo: descripción del motivo.
    """
    codigo_motivo = models.AutoField(primary_key=True)
    nombre_motivo = models.CharField(max_length=50, verbose_name="Nombre del motivo")

    class Meta:
        verbose_name = "Causa/Motivo"
        verbose_name_plural = "Causas/Motivos"
        ordering = ['nombre_motivo']
        db_table = 'causa_motivo'

    def __str__(self):
        return self.nombre_motivo

# =======================================================
# Modelo para gestionar servicios de salud prestados ====
# =======================================================

class ServicioSalud(models.Model):
    """
    Registra un encuentro o prestación de servicio de salud a un paciente.

    Campos y relaciones clave:
    - id_encuentro_paciente: clave primaria del encuentro.
    - id_paciente: paciente atendido.
    - id_prestadora: prestadora que brinda el servicio.
    - codigo_motivo, codigo_ingreso, modalidad_id: motivos y vía de ingreso.
    - id_huerfana, cie_id: diagnóstico y si corresponde a enfermedad huérfana.
    - tipo_servicio, fecha_ingreso, fecha_egreso: detalles del servicio.
    - diagnostico, diagnostico_egreso: textos diagnósticos.
    - estado_consulta: estado de la atención (programada, atendida, etc.).

    Este modelo se utiliza para llevar el historial de atención de pacientes.
    """
    ESTADO_CONSULTA_CHOICES = [
        ('PROGRAMADA', 'Programada'),
        ('ATENDIDA', 'Atendida'),
        ('CANCELADA', 'Cancelada'),
        ('NO_ASISTIO', 'No asistió'),
    ]

    id_encuentro_paciente = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,
                                    related_name='servicios_salud',
                                    verbose_name="Paciente")
    id_prestadora = models.ForeignKey(PrestadoraSalud, on_delete=models.PROTECT,
                                      verbose_name="Prestadora")
    codigo_motivo = models.ForeignKey(CausaMotivo, on_delete=models.PROTECT,
                                      verbose_name="Motivo")
    codigo_ingreso = models.ForeignKey(ViaIngreso, on_delete=models.PROTECT,
                                       verbose_name="Vía de ingreso")
    modalidad_id = models.ForeignKey(Modalidad, on_delete=models.PROTECT,
                                     verbose_name="Modalidad")
    id_huerfana = models.ForeignKey(CatalogoEnfermedadesHuerfanas, on_delete=models.SET_NULL,
                                    blank=True, null=True,
                                    verbose_name="Enfermedad huérfana")
    cie_id = models.ForeignKey(CIE10, on_delete=models.PROTECT,
                               verbose_name="Diagnóstico CIE-10")

    tipo_servicio = models.CharField(max_length=200, verbose_name="Tipo de servicio")
    fecha_ingreso = models.DateTimeField(verbose_name="Fecha de ingreso")
    fecha_egreso = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de egreso")
    diagnostico = models.CharField(max_length=500, verbose_name="Diagnóstico")
    diagnostico_egreso = models.CharField(max_length=500, blank=True, null=True,
                                          verbose_name="Diagnóstico de egreso")
    estado_consulta = models.CharField(max_length=100, choices=ESTADO_CONSULTA_CHOICES,
                                       default='PROGRAMADA', verbose_name="Estado de la consulta")

    class Meta:
        verbose_name = "Servicio de Salud"
        verbose_name_plural = "Servicios de Salud"
        ordering = ['-fecha_ingreso']
        db_table = 'servicio_salud'

    def __str__(self):
        return f"{self.id_paciente} - {self.tipo_servicio} ({self.fecha_ingreso.date()})"