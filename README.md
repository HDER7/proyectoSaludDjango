# Sistema de Gestión de Salud

Sistema web desarrollado en Django para la gestión integral de pacientes y servicios de salud, cumpliendo con los estándares del sector salud colombiano (Resolución 866 de 2021).

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Módulos Funcionales](#módulos-funcionales)
- [Base de Datos](#base-de-datos)
- [Uso del Sistema](#uso-del-sistema)
- [Comandos Útiles](#comandos-útiles)
- [Equipo de Desarrollo](#equipo-de-desarrollo)

## Descripción

El Sistema de Gestión de Salud es una aplicación web que permite administrar la información de pacientes y los servicios de salud prestados. El sistema incluye:

- Registro completo de pacientes con datos demográficos, laborales y de salud
- Gestión de servicios de salud con diagnósticos CIE-10
- Panel de administración avanzado con Jazzmin
- Búsquedas y filtros
- Interfaz intuitiva y responsiva con Bootstrap 5

## Características

### Módulo de Gestión de Pacientes
- **Crear** pacientes con información completa
- **Consultar** listado de pacientes con búsqueda
- **Actualizar** información de pacientes existentes
- **Eliminar** registros de pacientes

### Módulo de Servicios de Salud
- **Crear** registros de servicios prestados
- **Consultar** historial de servicios
- **Actualizar** información de servicios
-  **Eliminar** registros de servicios

### Funcionalidades Adicionales
- Dashboard con estadísticas en tiempo real
- Sistema de búsqueda avanzado
- Panel de administración personalizado (Django Admin + Jazzmin)
- Validación de datos y mensajes de confirmación
- Interfaz responsiva compatible con dispositivos móviles

## Tecnologías Utilizadas

- **Backend**: Python 3.x, Django 5.2.7
- **Base de Datos**: MySQL
- **Frontend**: HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Panel Admin**: Django Admin, django-jazzmin
- **Variables de Entorno**: python-dotenv

## Requisitos Previos

Antes de instalar el sistema, asegúrese de tener:

1. **Python 3.8 o superior**
   - Verificar: `python --version`

2. **MySQL 5.7 o superior**
   - Verificar: `mysql --version`

3. **pip** (Gestor de paquetes de Python)
   - Verificar: `pip --version`

## Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/proyectoSaludDjango.git
cd proyectoSaludDjango
```

### 2. Crear y Activar Entorno Virtual

**Windows:**
```bash
python -m venv clase_proyecto
clase_proyecto\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv clase_proyecto
source clase_proyecto/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install django==5.2.7
pip install mysqlclient
pip install python-dotenv
pip install django-jazzmin
```

### 4. Configurar Base de Datos

#### a) Crear la Base de Datos en MySQL

```sql
CREATE DATABASE ips
```

#### b) Configurar Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
USER=usuario_salud
PASS=tu_password
```

**IMPORTANTE**: Nunca subir el archivo `.env` a Git. Ya está incluido en `.gitignore`.

### 5. Ejecutar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Cargar Datos Iniciales

```bash
python manage.py cargar_datos_iniciales
```

Este comando carga automáticamente:
- Países
- Ciudades
- Ocupaciones CIUO
- Prestadoras de salud
- Diagnósticos CIE-10
- Y otros catálogos necesarios

### 7. Crear Superusuario (Si no existe)

```bash
python manage.py createsuperuser
```

**Datos por defecto del admin (si usaste cargar_datos_iniciales)**:
- Usuario: `admin`
- Email: `admin@gmail.com`
- Contraseña: `admin`

### 8. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

El sistema estará disponible en: **http://127.0.0.1:8000/**

## Estructura del Proyecto

```
proyectoSaludDjango/
│
├── gestion_salud/              # Aplicación principal
│   ├── management/             # Comandos personalizados
│   │   └── commands/
│   │       └── cargar_datos_iniciales.py
│   ├── migrations/             # Migraciones de base de datos
│   ├── templates/              # Templates HTML
│   │   └── gestion_salud/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── paciente_*.html
│   │       └── servicio_*.html
│   ├── admin.py                # Configuración del panel admin
│   ├── models.py               # Modelos de datos (17 modelos)
│   ├── views.py                # Vistas/Controladores (9 views)
│   └── apps.py
│
├── proyectoSaludDjango/        # Configuración del proyecto
│   ├── settings.py             # Configuración general
│   ├── urls.py                 # Enrutamiento de URLs (9 URLs)
│   └── wsgi.py
│
├── .env                        # Variables de entorno (NO subir a Git)
├── .gitignore                  # Archivos ignorados por Git
├── manage.py                   # Script de gestión de Django
├── MODELO_ER.md                # Documentación del modelo de datos
└── README.md                   # Este archivo
```

## Módulos Funcionales

### 1. Gestión de Pacientes

**URL Base**: `/pacientes/`

#### Endpoints (4 URLs):
1. `GET /pacientes/` - Listar pacientes con búsqueda
2. `GET/POST /pacientes/crear/` - Crear nuevo paciente
3. `GET/POST /pacientes/<id>/actualizar/` - Actualizar paciente
4. `GET/POST /pacientes/<id>/eliminar/` - Eliminar paciente

#### Campos del Paciente:
- **Identificación**: Tipo y número de documento (único)
- **Datos personales**: Nombres, apellidos, fecha de nacimiento, edad, sexo biológico, identidad de género
- **Ubicación**: País, ciudad/municipio
- **Datos culturales**: Etnia, comunidad étnica
- **Datos laborales**: Ocupación CIUO
- **Datos de salud**: Prestadora de salud, discapacidades
- **Auditoría**: Fechas de creación y actualización automáticas

### 2. Gestión de Servicios de Salud

**URL Base**: `/servicios/`

#### Endpoints (4 URLs):
1. `GET /servicios/` - Listar servicios con búsqueda
2. `GET/POST /servicios/crear/` - Crear nuevo servicio
3. `GET/POST /servicios/<id>/actualizar/` - Actualizar servicio
4. `GET/POST /servicios/<id>/eliminar/` - Eliminar servicio

#### Campos del Servicio:
- **Paciente**: Paciente que recibe el servicio
- **Prestadora**: Entidad que presta el servicio
- **Tipo de servicio**: Consulta, urgencia, hospitalización, etc.
- **Diagnóstico**: CIE-10 y descripción detallada
- **Fechas**: Ingreso y egreso
- **Estado**: Programada, Atendida, Cancelada, No asistió
- **Motivo y vía de ingreso**: Según catálogos estándar

### 3. Página de Inicio

**URL**: `/` (1 URL)

Dashboard que muestra:
- Total de pacientes registrados
- Total de servicios prestados
- Últimos 5 servicios recientes
- Accesos rápidos a todas las funcionalidades

### 4. Panel de Administración

**URL**: `/admin/`

Panel avanzado con interfaz Jazzmin que permite:
- Gestión completa de todos los 17 modelos
- Búsqueda y filtrado avanzado
- Gestión de usuarios y permisos
- Visualización mejorada con Jazzmin theme

## Base de Datos

### Estructura Principal

El sistema utiliza MySQL con 17 tablas principales. Ver [MODELO_ER.md](MODELO_ER.md) para el diagrama completo.

#### Tablas Principales:
1. **paciente** - Información de pacientes (tabla central)
2. **servicio_salud** - Registros de servicios prestados
3. **prestadora_salud** - EPS, IPS y otras entidades
4. **cie10** - Clasificación Internacional de Enfermedades
5. **pais**, **ciudad** - Catálogos geográficos
6. **ocupacion_ciuo** - Clasificación de ocupaciones
7. **etnia**, **comunidad_etnica** - Datos culturales
8. **discapacidad** - Tipos de discapacidad
9. **causa_motivo**, **via_ingreso**, **modalidad** - Catálogos de servicios
10. **voluntad_anticipada**, **oposicion_donacion** - Voluntades del paciente
11. **paciente_nacionalidad**, **paciente_discapacidad** - Tablas intermedias M:N

### Total de URLs: 9

1. `/` - Página de inicio
2. `/pacientes/` - Listar pacientes
3. `/pacientes/crear/` - Crear paciente
4. `/pacientes/<id>/actualizar/` - Actualizar paciente
5. `/pacientes/<id>/eliminar/` - Eliminar paciente
6. `/servicios/` - Listar servicios
7. `/servicios/crear/` - Crear servicio
8. `/servicios/<id>/actualizar/` - Actualizar servicio
9. `/servicios/<id>/eliminar/` - Eliminar servicio

*(Además del `/admin/` para el panel de administración)*

## Uso del Sistema

### 1. Acceder al Sistema

Abrir navegador en: http://127.0.0.1:8000/

### 2. Registrar un Paciente

1. Click en "Pacientes" en el menú o "Registrar Paciente" en el dashboard
2. Completar todos los campos requeridos (*)
3. Click en "Guardar Paciente"
4. El sistema muestra confirmación de éxito

### 3. Registrar un Servicio

1. Click en "Servicios" en el menú o "Nuevo Servicio" en el dashboard
2. Seleccionar paciente existente
3. Completar información del servicio, diagnóstico y fechas
4. Click en "Guardar Servicio"

### 4. Búsqueda

- **Pacientes**: Buscar por documento, nombre o apellido
- **Servicios**: Buscar por paciente, documento o tipo de servicio

### 5. Panel de Administración

1. Acceder a http://127.0.0.1:8000/admin/
2. Iniciar sesión con:
   - Usuario: `admin`
   - Contraseña: `admin`
3. Gestionar catálogos y todos los datos del sistema

## Comandos Útiles

### Django Management

```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Cargar datos iniciales
python manage.py cargar_datos_iniciales

# Abrir shell interactivo
python manage.py shell

# Verificar problemas
python manage.py check

# Limpiar sesiones expiradas
python manage.py clearsessions
```

### Base de Datos

```bash
# Exportar base de datos
mysqldump -u usuario_salud -p ips > backup_ips.sql

# Importar base de datos
mysql -u usuario_salud -p ips < backup_ips.sql
```

## Solución de Problemas Comunes

### Error de Conexión a MySQL

**Problema**: `django.db.utils.OperationalError: (2003, "Can't connect to MySQL server...")`

**Solución**:
1. Verificar que MySQL esté ejecutándose
2. Verificar credenciales en `.env`
3. Verificar que la base de datos `ips` exista

### Puerto 8000 en Uso

**Problema**: `Error: That port is already in use.`

**Solución**:
```bash
# Usar otro puerto
python manage.py runserver 8080

# O matar el proceso en Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Error al Cargar Datos

**Problema**: Error al ejecutar `cargar_datos_iniciales`

**Solución**:
1. Asegurarse de que las migraciones se hayan ejecutado: `python manage.py migrate`
2. Verificar que la base de datos esté accesible

