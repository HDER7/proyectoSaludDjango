
# 🏥 Proyecto — Historia Clínica Electrónica

Este sistema permite gestionar la historia clínica electrónica de pacientes conforme a la Resolución 866 de 2021 del Ministerio de Salud de Colombia.

## 🚀 Requisitos

- Python 3.10+
- Django 4.x
- MySQL Server
- Conexión configurada en `settings.py` con `ENGINE = 'django.db.backends.mysql'`

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://tu-repo.git
   cd salud

2. Instala las dependencias:
    pip install -r requirements.txt

3. configura la base de datos en settings.py:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'salud_db',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

4. Ejecuta las migraciones en el Bash
    python manage.py makemigrations
    python manage.py migrate

5. Cargar los datos iniciales
    Una vez que las tablas existan, ejecuta el comando personalizado:
    ```bash
   python manage.py cargar_datos_iniciales

6. Ejecuta el proyecto

    python manage.py runserver

7. Datos del admin por defecto para ingresar:
    username='admin',
    email='admin@gmail.com',
    password='admin'