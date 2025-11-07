from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Paciente, ServicioSalud, PrestadoraSalud, Pais, Ciudad, OcupacionCIUO, ComunidadEtnica, Etnia, CIE10, Modalidad, CausaMotivo, ViaIngreso, PacienteNacionalidad


def index(request):
    """Vista principal del sistema"""
    total_pacientes = Paciente.objects.count()
    total_servicios = ServicioSalud.objects.count()
    servicios_recientes = ServicioSalud.objects.select_related('id_paciente', 'id_prestadora').order_by('-fecha_ingreso')[:5]

    context = {
        'total_pacientes': total_pacientes,
        'total_servicios': total_servicios,
        'servicios_recientes': servicios_recientes,
    }
    return render(request, '../templates/index.html', context)


def paciente_listar(request):
    """Lista todos los pacientes con búsqueda"""
    query = request.GET.get('q', '')
    pacientes = Paciente.objects.select_related(
        'id_paciente_pais', 'codigo_municipio', 'id_prestadora'
    ).all()

    if query:
        pacientes = pacientes.filter(
            Q(numero_documento__icontains=query) |
            Q(primer_nombre__icontains=query) |
            Q(primer_apellido__icontains=query)
        )

    pacientes = pacientes.order_by('-fecha_creacion')

    context = {
        'pacientes': pacientes,
        'query': query,
    }
    return render(request, '../templates/paciente_listar.html', context)


def paciente_crear(request):
    """Crea un nuevo paciente"""
    if request.method == 'POST':
        try:
            # Crear el paciente SIN nacionalidad primero (para evitar dependencia circular)
            paciente = Paciente.objects.create(
                tipo_documento=request.POST['tipo_documento'],
                numero_documento=request.POST['numero_documento'],
                primer_nombre=request.POST['primer_nombre'],
                segundo_nombre=request.POST.get('segundo_nombre', ''),
                primer_apellido=request.POST['primer_apellido'],
                segundo_apellido=request.POST.get('segundo_apellido', ''),
                fecha_nacimiento=request.POST['fecha_nacimiento'],
                edad=request.POST['edad'],
                sexo_biologico=request.POST['sexo_biologico'],
                identidad_genero=request.POST.get('identidad_genero', ''),
                id_paciente_pais_id=request.POST['id_paciente_pais'],
                codigo_municipio_id=request.POST['codigo_municipio'],
                codigo_CIUO_id=request.POST['codigo_CIUO'],
                id_comunidad_id=request.POST['id_comunidad'],
                id_etnia_id=request.POST['id_etnia'],
                id_prestadora_id=request.POST['id_prestadora'],
            )

            # Crear la nacionalidad del paciente
            nacionalidad = PacienteNacionalidad.objects.create(
                id_paciente=paciente,
                id_pais_id=request.POST['id_nacionalidad']
            )

            # Actualizar el paciente con la nacionalidad creada
            paciente.id_nacionalidad = nacionalidad
            paciente.save()

            messages.success(request, f'Paciente {paciente.primer_nombre} {paciente.primer_apellido} creado exitosamente.')
            return redirect('paciente_listar')

        except Exception as e:
            messages.error(request, f'Error al crear el paciente: {str(e)}')

    # Obtener datos para los formularios
    context = {
        'paises': Pais.objects.all(),
        'ciudades': Ciudad.objects.all(),
        'ocupaciones': OcupacionCIUO.objects.all(),
        'comunidades': ComunidadEtnica.objects.all(),
        'etnias': Etnia.objects.all(),
        'prestadoras': PrestadoraSalud.objects.all(),
    }
    return render(request, '../templates/paciente_crear.html', context)


def paciente_actualizar(request, pk):
    """Actualiza un paciente existente"""
    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':
        try:
            paciente.tipo_documento = request.POST['tipo_documento']
            paciente.numero_documento = request.POST['numero_documento']
            paciente.primer_nombre = request.POST['primer_nombre']
            paciente.segundo_nombre = request.POST.get('segundo_nombre', '')
            paciente.primer_apellido = request.POST['primer_apellido']
            paciente.segundo_apellido = request.POST.get('segundo_apellido', '')
            paciente.fecha_nacimiento = request.POST['fecha_nacimiento']
            paciente.edad = request.POST['edad']
            paciente.sexo_biologico = request.POST['sexo_biologico']
            paciente.identidad_genero = request.POST.get('identidad_genero', '')
            paciente.id_paciente_pais_id = request.POST['id_paciente_pais']
            paciente.codigo_municipio_id = request.POST['codigo_municipio']
            paciente.codigo_CIUO_id = request.POST['codigo_CIUO']
            paciente.id_comunidad_id = request.POST['id_comunidad']
            paciente.id_etnia_id = request.POST['id_etnia']
            paciente.id_prestadora_id = request.POST['id_prestadora']

            # Actualizar o crear la nacionalidad
            nuevo_pais_id = request.POST['id_nacionalidad']

            if paciente.id_nacionalidad:
                # Si ya tiene una nacionalidad, actualizar el país
                paciente.id_nacionalidad.id_pais_id = nuevo_pais_id
                paciente.id_nacionalidad.save()
            else:
                # Si no tiene nacionalidad, crear una nueva
                nacionalidad = PacienteNacionalidad.objects.create(
                    id_paciente=paciente,
                    id_pais_id=nuevo_pais_id
                )
                paciente.id_nacionalidad = nacionalidad

            paciente.save()

            messages.success(request, f'Paciente {paciente.primer_nombre} {paciente.primer_apellido} actualizado exitosamente.')
            return redirect('paciente_listar')

        except Exception as e:
            messages.error(request, f'Error al actualizar el paciente: {str(e)}')

    context = {
        'paciente': paciente,
        'paises': Pais.objects.all(),
        'ciudades': Ciudad.objects.all(),
        'ocupaciones': OcupacionCIUO.objects.all(),
        'comunidades': ComunidadEtnica.objects.all(),
        'etnias': Etnia.objects.all(),
        'prestadoras': PrestadoraSalud.objects.all(),
    }
    return render(request, '../templates/paciente_actualizar.html', context)


def paciente_eliminar(request, pk):
    """Elimina un paciente"""
    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':
        nombre_completo = f"{paciente.primer_nombre} {paciente.primer_apellido}"
        try:
            # Primero quitar la referencia a nacionalidad
            paciente.id_nacionalidad = None
            paciente.save()
            # Luego eliminar los registros relacionados de nacionalidades
            paciente.nacionalidades.all().delete()
            # Finalmente eliminar el paciente
            paciente.delete()
            messages.success(request, f'Paciente {nombre_completo} eliminado exitosamente.')
            return redirect('paciente_listar')
        except Exception as e:
            messages.error(request, f'Error al eliminar el paciente: {str(e)}')

    context = {
        'paciente': paciente,
    }
    return render(request, '../templates/paciente_eliminar.html', context)



def servicio_listar(request):
    """Lista todos los servicios de salud"""
    query = request.GET.get('q', '')
    servicios = ServicioSalud.objects.select_related(
        'id_paciente', 'id_prestadora', 'cie_id', 'modalidad_id'
    ).all()

    if query:
        servicios = servicios.filter(
            Q(id_paciente__numero_documento__icontains=query) |
            Q(id_paciente__primer_nombre__icontains=query) |
            Q(id_paciente__primer_apellido__icontains=query) |
            Q(tipo_servicio__icontains=query)
        )

    servicios = servicios.order_by('-fecha_ingreso')

    context = {
        'servicios': servicios,
        'query': query,
    }
    return render(request, '../templates/servicio_listar.html', context)


def servicio_crear(request):
    """Crea un nuevo servicio de salud"""
    if request.method == 'POST':
        try:
            servicio = ServicioSalud.objects.create(
                id_paciente_id=request.POST['id_paciente'],
                id_prestadora_id=request.POST['id_prestadora'],
                codigo_motivo_id=request.POST['codigo_motivo'],
                codigo_ingreso_id=request.POST['codigo_ingreso'],
                modalidad_id_id=request.POST['modalidad_id'],
                cie_id_id=request.POST['cie_id'],
                tipo_servicio=request.POST['tipo_servicio'],
                fecha_ingreso=request.POST['fecha_ingreso'],
                fecha_egreso=request.POST.get('fecha_egreso') or None,
                diagnostico=request.POST['diagnostico'],
                diagnostico_egreso=request.POST.get('diagnostico_egreso', ''),
                estado_consulta=request.POST['estado_consulta'],
            )

            messages.success(request, 'Servicio de salud creado exitosamente.')
            return redirect('servicio_listar')

        except Exception as e:
            messages.error(request, f'Error al crear el servicio: {str(e)}')

    context = {
        'pacientes': Paciente.objects.all().order_by('primer_apellido', 'primer_nombre'),
        'prestadoras': PrestadoraSalud.objects.all(),
        'motivos': CausaMotivo.objects.all(),
        'vias_ingreso': ViaIngreso.objects.all(),
        'modalidades': Modalidad.objects.all(),
        'diagnosticos': CIE10.objects.all(),
    }
    return render(request, '../templates/servicio_crear.html', context)


def servicio_actualizar(request, pk):
    """Actualiza un servicio de salud existente"""
    servicio = get_object_or_404(ServicioSalud, pk=pk)

    if request.method == 'POST':
        try:
            servicio.id_paciente_id = request.POST['id_paciente']
            servicio.id_prestadora_id = request.POST['id_prestadora']
            servicio.codigo_motivo_id = request.POST['codigo_motivo']
            servicio.codigo_ingreso_id = request.POST['codigo_ingreso']
            servicio.modalidad_id_id = request.POST['modalidad_id']
            servicio.cie_id_id = request.POST['cie_id']
            servicio.tipo_servicio = request.POST['tipo_servicio']
            servicio.fecha_ingreso = request.POST['fecha_ingreso']
            servicio.fecha_egreso = request.POST.get('fecha_egreso') or None
            servicio.diagnostico = request.POST['diagnostico']
            servicio.diagnostico_egreso = request.POST.get('diagnostico_egreso', '')
            servicio.estado_consulta = request.POST['estado_consulta']

            servicio.save()

            messages.success(request, 'Servicio de salud actualizado exitosamente.')
            return redirect('servicio_listar')

        except Exception as e:
            messages.error(request, f'Error al actualizar el servicio: {str(e)}')

    context = {
        'servicio': servicio,
        'pacientes': Paciente.objects.all().order_by('primer_apellido', 'primer_nombre'),
        'prestadoras': PrestadoraSalud.objects.all(),
        'motivos': CausaMotivo.objects.all(),
        'vias_ingreso': ViaIngreso.objects.all(),
        'modalidades': Modalidad.objects.all(),
        'diagnosticos': CIE10.objects.all(),
    }
    return render(request, '../templates/servicio_actualizar.html', context)


def servicio_eliminar(request, pk):
    """Elimina un servicio de salud"""
    servicio = get_object_or_404(ServicioSalud, pk=pk)

    if request.method == 'POST':
        try:
            servicio.delete()
            messages.success(request, 'Servicio de salud eliminado exitosamente.')
            return redirect('servicio_listar')
        except Exception as e:
            messages.error(request, f'Error al eliminar el servicio: {str(e)}')

    context = {
        'servicio': servicio,
    }
    return render(request, '../templates/servicio_eliminar.html', context)
