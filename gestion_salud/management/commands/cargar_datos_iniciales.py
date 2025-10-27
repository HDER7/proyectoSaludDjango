from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from gestion_salud.models import (
    Pais, Ciudad, OcupacionCIUO, ComunidadEtnica, Etnia,
    Discapacidad, Modalidad, ViaIngreso, CausaMotivo,
    CatalogoEnfermedadesHuerfanas, CIE10
)


class Command(BaseCommand):
    help = 'Carga datos iniciales en la base de datos'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando carga de datos...'))

        # Países
        if Pais.objects.count() == 0:
            Pais.objects.bulk_create([
                Pais(pais_name='Colombia'),
                Pais(pais_name='México'),
                Pais(pais_name='Argentina'),
                Pais(pais_name='Estados Unidos'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Países creados'))

        # Ciudades
        if Ciudad.objects.count() == 0:
            Ciudad.objects.bulk_create([
                Ciudad(nombre='Bogotá'),
                Ciudad(nombre='Medellín'),
                Ciudad(nombre='Cali'),
                Ciudad(nombre='Barranquilla'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Ciudades creadas'))

        # Ocupaciones CIUO
        if OcupacionCIUO.objects.count() == 0:
            OcupacionCIUO.objects.bulk_create([
                OcupacionCIUO(nombre_ocupacion='Ingeniero de sistemas'),
                OcupacionCIUO(nombre_ocupacion='Enfermero'),
                OcupacionCIUO(nombre_ocupacion='Médico general'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Ocupaciones creadas'))

        # Etnias
        if Etnia.objects.count() == 0:
            Etnia.objects.bulk_create([
                Etnia(etnia='AF'),
                Etnia(etnia='IN'),
                Etnia(etnia='RA'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Etnias creadas'))

        # Comunidades étnicas
        if ComunidadEtnica.objects.count() == 0:
            ComunidadEtnica.objects.bulk_create([
                ComunidadEtnica(comunidad='001'),
                ComunidadEtnica(comunidad='002'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Comunidades étnicas creadas'))

        # Discapacidades
        if Discapacidad.objects.count() == 0:
            Discapacidad.objects.bulk_create([
                Discapacidad(cod_categoria_discapacidad='01', nombre_discapacidad='Física'),
                Discapacidad(cod_categoria_discapacidad='02', nombre_discapacidad='Auditiva'),
                Discapacidad(cod_categoria_discapacidad='03', nombre_discapacidad='Visual'),
                Discapacidad(cod_categoria_discapacidad='04', nombre_discapacidad='Sordoceguera'),
                Discapacidad(cod_categoria_discapacidad='05', nombre_discapacidad='Intelectual'),
                Discapacidad(cod_categoria_discapacidad='06', nombre_discapacidad='Psicosocial (mental)'),
                Discapacidad(cod_categoria_discapacidad='07', nombre_discapacidad='Múltiple'),
                Discapacidad(cod_categoria_discapacidad='08', nombre_discapacidad='Ninguna'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Discapacidades creadas'))

        # Modalidades
        if Modalidad.objects.count() == 0:
            Modalidad.objects.bulk_create([
                Modalidad(grupo_servicio='01'),
                Modalidad(grupo_servicio='02'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Modalidades creadas'))

        # Vías de ingreso
        if ViaIngreso.objects.count() == 0:
            ViaIngreso.objects.bulk_create([
                ViaIngreso(nombre_ingreso='01'),
                ViaIngreso(nombre_ingreso='02'),
                ViaIngreso(nombre_ingreso='03'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Vías de ingreso creadas'))

        # Causas/Motivos
        if CausaMotivo.objects.count() == 0:
            CausaMotivo.objects.bulk_create([
                CausaMotivo(nombre_motivo='10'),
                CausaMotivo(nombre_motivo='11'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Causas/Motivos creadas'))

        # Enfermedades huérfanas
        if CatalogoEnfermedadesHuerfanas.objects.count() == 0:
            CatalogoEnfermedadesHuerfanas.objects.bulk_create([
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Marfan', tipo='A1'),
                CatalogoEnfermedadesHuerfanas(nombre='Fibrosis quística', tipo='B2'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Ehlers-Danlos', tipo='A3'),
                CatalogoEnfermedadesHuerfanas(nombre='Esclerosis lateral amiotrófica', tipo='A4'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Rett', tipo='A5'),
                CatalogoEnfermedadesHuerfanas(nombre='Ataxia de Friedreich', tipo='A6'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Prader-Willi', tipo='A7'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Angelman', tipo='A8'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Turner', tipo='A9'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Noonan', tipo='B1'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Williams', tipo='B3'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Alport', tipo='B4'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Sjögren', tipo='B5'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Cushing', tipo='B6'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Klinefelter', tipo='B7'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de X frágil', tipo='B8'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Leigh', tipo='B9'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Dravet', tipo='C1'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Moebius', tipo='C2'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Joubert', tipo='C3'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Alström', tipo='C4'),
                CatalogoEnfermedadesHuerfanas(nombre='Síndrome de Bardet-Biedl', tipo='C5'),
            ])
            self.stdout.write(self.style.SUCCESS('✓ Enfermedades huérfanas creadas'))

        # Diagnósticos CIE-10
        if CIE10.objects.count() == 0:
            CIE10.objects.bulk_create([
                CIE10(nombre='Diabetes mellitus tipo 2', tipo='11'),
                CIE10(nombre='Hipertensión esencial', tipo='10'),
                CIE10(nombre='Fiebre tifoidea', tipo='01'),
                CIE10(nombre='Enteritis debida a Salmonella', tipo='02'),
                CIE10(nombre='Shigelosis debida a Shigella dysenteriae', tipo='30'),
                CIE10(nombre='Shigelosis debida a Shigella flexneri', tipo='31'),
                CIE10(nombre='Shigelosis debida a Shigella boydii', tipo='32'),
                CIE10(nombre='Shigelosis debida a Shigella sonnei', tipo='33'),
                CIE10(nombre='Infección debida a Escherichia coli enteropatógena', tipo='40'),
                CIE10(nombre='Tuberculosis pulmonar, confirmada bacteriológicamente', tipo='50'),
                CIE10(nombre='Tuberculosis pulmonar, no confirmada bacteriológicamente', tipo='51'),
                CIE10(nombre='Tuberculosis de otros órganos respiratorios', tipo='52'),
                CIE10(nombre='Tuberculosis miliar', tipo='59'),
                CIE10(nombre='Varicela sin complicaciones', tipo='01'),
                CIE10(nombre='Sarampión sin complicaciones', tipo='05'),
                CIE10(nombre='Rubeola sin complicaciones', tipo='06'),
                CIE10(nombre='Hepatitis viral aguda tipo A', tipo='15'),
                CIE10(nombre='Hepatitis viral aguda tipo B', tipo='16'),
                CIE10(nombre='Hepatitis viral aguda tipo C', tipo='17'),
                CIE10(nombre='Hepatitis viral crónica tipo B', tipo='18'),
                CIE10(nombre='Hepatitis viral crónica tipo C', tipo='82'),
                CIE10(nombre='VIH con infección sintomática', tipo='20')
            ])
            self.stdout.write(self.style.SUCCESS('✓ Diagnósticos CIE-10 creados'))

        # Crear usuario administrador
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@gmail.com',
                password='admin'
            )
            self.stdout.write(self.style.SUCCESS('✓ Usuario administrador creado'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Usuario administrador ya existe'))

        self.stdout.write(self.style.SUCCESS('\n¡Carga de datos completada exitosamente!'))