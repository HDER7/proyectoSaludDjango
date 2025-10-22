from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Modelos basicos
class Pais(models.Model):
    """Modelo para gestionar paises"""
    id_pais = models.AutoField(primary_key=True)
    pais_name = models.CharField(max_length=200, verbose_name="Nombre del pais")

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ['pais_name']
        db_table = 'pais'

    def __str__(self):
        return self.pais_name


class Ciudad(models.Model):
    """Modelo para gestionar ciudades"""
    codigo_municipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la ciudad")

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ['nombre']
        db_table = 'ciudad'

    def __str__(self):
        return self.nombre


class OcupacionCIUO(models.Model):
    """Clasificacion internacional de ocupacion"""
    codigo_CIUO = models.AutoField(primary_key=True)
    nombre_ocupacion = models.CharField(max_length=200, verbose_name="Nombre de la ocupacion")

    class Meta:
        verbose_name = "Ocupacion CIUO"
        verbose_name_plural = "Ocupaciones CIUO"
        ordering = ['nombre_ocupacion']
        db_table = 'ocupacion_ciuo'


class ComunidadEtnica(models.Model):
    """Modelo para gestionar comunidades de etnicas"""
    id_comunidad =  models.AutoField(primary_key=True)
    comunidad = models.CharField(max_length=3, verbose_name="Codigo de la comunidad")

    class Meta:
        verbose_name = "Comunidad Etnica"
        verbose_name_plural = "Comunidades Etnicas"
        ordering = ['comunidad']
        db_table = 'comunidad_etnica'


class Etnia(models.Model):
    """Modelo para gestionar etnias"""
    ETNIAS = [
        ('01','Indigena'),
        ('02','Rom(Gitano)'),
        ('03', 'Raizal(San Andres y providencia)'),
        ('04', 'Palenquero de san basilio de palenque'),
        ('05', 'Negro'),
        ('06', 'Afrodecendiente'),
        ('99', 'Ninguno')
    ]
    id_etnia = models.AutoField(primary_key=True)
    etnia = models.CharField(max_length=2, choices=ETNIAS, verbose_name="Codigo de la etnia")

    class Meta:
        verbose_name = "Etnia"
        verbose_name_plural = "Etnias"
        ordering = ['etnia']
        db_table = 'etnia'

    def __str__(self):
        return self.etnia


class PrestadoraSalud(models.Model):
    """Modelo para gestionar prestadoras de salud (EPS, IPS, etc.)"""
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


class Discapacidad(models.Model):
    """Modelo para gestionar tipos de discapacidad"""
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


class VoluntadAnticipada(models.Model):
    """Modelo para gestionar voluntades anticipadas"""
    ESTADOS = [
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
    estado_voluntad = models.CharField(max_length=10, choices=ESTADOS,
                                       default='ACTIVA', verbose_name="Estado de la voluntad")
    firma_paciente = models.CharField(max_length=100, verbose_name="Firma del paciente")

    class Meta:
        verbose_name = "Voluntad Anticipada"
        verbose_name_plural = "Voluntades Anticipadas"
        ordering = ['-fecha_suscripcion']
        db_table = 'voluntad_anticipada'

    def __str__(self):
        return f"Voluntad de {self.id_paciente} - {self.estado_voluntad}"


class OposicionDonacion(models.Model):
    """Modelo para gestionar oposición a donación de órganos"""
    id_oposicion = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE,
                                    related_name='oposiciones_donacion',
                                    verbose_name="Paciente")
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


# Modelos Principales

class Paciente(models.Model):
    """Modelo principal para gestionar información de pacientes"""
    TIPO_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ('RC', 'Registro Civil'),
        ('CN', 'Certificado de Nacido Vivo'),
        ('CD', 'Carné Diplomático'),
        ('SC', 'Salvoconducto de Permanencia'),
        ('PR', 'Pasaporte de la ONU'),
        ('PE', 'Permiso Especial de Permanencia'),
        ('AS', 'Adulto Sin Identificación'),
        ('MS', 'Menor Sin Identificación'),
        ('PT', 'Permiso por Protección Temporal'),
        ('DE', 'Documento Extranjero'),
        ('SI', 'Sin Identificación'),
        ('NV', 'Certificado Nacido Vivo'),
        ('NI', 'NIT'),
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
    tipo_documento = models.CharField(max_length=5, choices=TIPO_DOCUMENTO,
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


class PacienteNacionalidad(models.Model):
    """Modelo intermedio para gestionar nacionalidades de pacientes"""
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


class PacienteDiscapacidad(models.Model):
    """Modelo intermedio para gestionar discapacidades de pacientes"""
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


# Modelos de servicios de salud

class CIE10(models.Model):
    """Clasificación Internacional de Enfermedades"""
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


class Modalidad(models.Model):
    """Modelo para modalidades de atención"""
    modalidad_id = models.AutoField(primary_key=True)
    grupo_servicio = models.CharField(max_length=2, verbose_name="Grupo de servicio")

    class Meta:
        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"
        ordering = ['grupo_servicio']
        db_table = 'modalidad'

    def __str__(self):
        return self.grupo_servicio


class CatalogoEnfermedadesHuerfanas(models.Model):
    """Catálogo de enfermedades huérfanas o raras"""
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


class ViaIngreso(models.Model):
    """Vías de ingreso al sistema de salud"""
    codigo_ingreso = models.AutoField(primary_key=True)
    nombre_ingreso = models.CharField(max_length=50, verbose_name="Nombre del ingreso")

    class Meta:
        verbose_name = "Vía de Ingreso"
        verbose_name_plural = "Vías de Ingreso"
        ordering = ['nombre_ingreso']
        db_table = 'via_ingreso'

    def __str__(self):
        return self.nombre_ingreso


class CausaMotivo(models.Model):
    """Causas o motivos de consulta"""
    codigo_motivo = models.AutoField(primary_key=True)
    nombre_motivo = models.CharField(max_length=50, verbose_name="Nombre del motivo")

    class Meta:
        verbose_name = "Causa/Motivo"
        verbose_name_plural = "Causas/Motivos"
        ordering = ['nombre_motivo']
        db_table = 'causa_motivo'

    def __str__(self):
        return self.nombre_motivo


class ServicioSalud(models.Model):
    """Modelo para gestionar servicios de salud prestados"""
    ESTADO_CONSULTA = [
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
    estado_consulta = models.CharField(max_length=100, choices=ESTADO_CONSULTA,
                                       default='PROGRAMADA', verbose_name="Estado de la consulta")

    class Meta:
        verbose_name = "Servicio de Salud"
        verbose_name_plural = "Servicios de Salud"
        ordering = ['-fecha_ingreso']
        db_table = 'servicio_salud'

    def __str__(self):
        return f"{self.id_paciente} - {self.tipo_servicio} ({self.fecha_ingreso.date()})"