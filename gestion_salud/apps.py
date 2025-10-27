from django.apps import AppConfig
from django.db.utils import OperationalError
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import get_user_model

class GestionSaludConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion_salud'

    def ready(self):
        from gestion_salud.models import (
            Pais, Ciudad, OcupacionCIUO, ComunidadEtnica, Etnia,
            Discapacidad, Modalidad, ViaIngreso, CausaMotivo,
            CatalogoEnfermedadesHuerfanas, CIE10
        )

        try:
            # ======================================================
            # Poblar tablas con datos iniciales ====================
            # ======================================================

            # Países
            if Pais.objects.count() == 0:
                Pais.objects.bulk_create([
                    Pais(pais_name='Colombia'),
                    Pais(pais_name='México'),
                    Pais(pais_name='Argentina'),
                    Pais(pais_name='Estados Unidos'),
                ])

            # Ciudades
            if Ciudad.objects.count() == 0:
                Ciudad.objects.bulk_create([
                    Ciudad(nombre='Bogotá'),
                    Ciudad(nombre='Medellín'),
                    Ciudad(nombre='Cali'),
                    Ciudad(nombre='Barranquilla'),
                ])

            # Ocupaciones CIUO
            if OcupacionCIUO.objects.count() == 0:
                OcupacionCIUO.objects.bulk_create([
                    OcupacionCIUO(nombre_ocupacion='Ingeniero de sistemas'),
                    OcupacionCIUO(nombre_ocupacion='Enfermero'),
                    OcupacionCIUO(nombre_ocupacion='Médico general'),
                ])

            # Etnias
            if Etnia.objects.count() == 0:
                Etnia.objects.bulk_create([
                    Etnia(etnia='AF'),
                    Etnia(etnia='IN'),
                    Etnia(etnia='RA'),
                ])

            # Comunidades étnicas
            if ComunidadEtnica.objects.count() == 0:
                ComunidadEtnica.objects.bulk_create([
                    ComunidadEtnica(comunidad='001'),
                    ComunidadEtnica(comunidad='002'),
                ])

            # Discapacidades
            if Discapacidad.objects.count() == 0:
                Discapacidad.objects.bulk_create([
                    Discapacidad(cod_categoria_discapacidad='01', nombre_discapacidad='Física'),
                    Discapacidad(cod_categoria_discapacidad='02', nombre_discapacidad='Auditiva'),
                ])

            # Modalidades
            if Modalidad.objects.count() == 0:
                Modalidad.objects.bulk_create([
                    Modalidad(grupo_servicio='01'),
                    Modalidad(grupo_servicio='02'),
                ])

            # Vías de ingreso
            if ViaIngreso.objects.count() == 0:
                ViaIngreso.objects.bulk_create([
                    ViaIngreso(nombre_ingreso='01'),
                    ViaIngreso(nombre_ingreso='02'),
                ])

            # Causas/Motivos
            if CausaMotivo.objects.count() == 0:
                CausaMotivo.objects.bulk_create([
                    CausaMotivo(nombre_motivo='10'),
                    CausaMotivo(nombre_motivo='11'),
                ])

            # Enfermedades huérfanas
            if CatalogoEnfermedadesHuerfanas.objects.count() == 0:
                CatalogoEnfermedadesHuerfanas.objects.bulk_create([
                    CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Marfan', tipo='A1'),
                    CatalogoEnfermedadesHuerfanas(nombre='Fibrosis quística', tipo='B2'),
                ])

            # Diagnósticos CIE-10
            if CIE10.objects.count() == 0:
                CIE10.objects.bulk_create([
                    CIE10(nombre='Diabetes mellitus tipo 2', tipo='E11'),
                    CIE10(nombre='Hipertensión esencial', tipo='I10'),
                ])

            # ======================================================
            # Crear usuario administrador por defecto ==============
            # ======================================================

            User = get_user_model()

            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@saludyvida.local',
                    password='admin123'
                )

        except (OperationalError, ObjectDoesNotExist):
            pass  # Evita errores si la base de datos aún no está migrada