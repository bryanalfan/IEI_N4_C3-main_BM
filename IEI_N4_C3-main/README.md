# IEI_N4_C3 - Aplicación Django

Proyecto de evaluación correspondiente a la construcción de una aplicación sencilla con Django.

## 1. Crear el ambiente virtual

Desde la carpeta raíz del proyecto:

```bash
python -m venv venv
```

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación:

```powershell
Set-ExecutionPolicy Bypass -Scope CurrentUser
```

Para salir del ambiente virtual:

```bash
deactivate
```

## 2. Instalar dependencias

Con el ambiente virtual activado:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

La dependencia principal es Django 6.1, utilizada para construir y ejecutar la aplicación web.

## 3. Ejecutar el proyecto

```bash
python manage.py check
python manage.py test
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## 4. Probar el error 404

Con el servidor ejecutándose, ingresar a una ruta que no exista, por ejemplo:

```text
http://127.0.0.1:8000/ruta-que-no-existe/
```

La aplicación debe mostrar la plantilla personalizada `incidencias/templates/404.html`.

> `DEBUG` está configurado en `False` y `ALLOWED_HOSTS` incluye `127.0.0.1` y `localhost` para que el controlador 404 personalizado pueda verificarse durante la ejecución local.

## 5. Estructura principal

```text
IEI_N4_C3-main/
├── manage.py
├── requirements.txt
├── README.md
├── RESPUESTAS_RUBRICA.md
├── drf/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── incidencias/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── migrations/
    │   └── __init__.py
    └── templates/
        ├── bienvenida.html
        └── 404.html
```

## 6. Relación con la rúbrica

- **Variables y tipos:** `nombre`, `cantidad_incidencias`, `incidencias_resueltas` e `incidencias_pendientes`.
- **Operaciones:** resta para calcular pendientes y comparación `>` para evaluar el estado.
- **Estructuras de control:** `if/else` en la vista principal.
- **Integración:** las variables de Python se envían a `bienvenida.html` mediante el contexto de `render()`.
- **Django:** proyecto `drf` y aplicación `incidencias` correctamente configurados.
- **Ruta de bienvenida:** `/` → `views.bienvenida` → `bienvenida.html`.
- **Error 404:** `handler404` → `views.error_404` → `404.html`.
- **Dependencias:** registradas en `requirements.txt`.

Las respuestas desarrolladas para las cuatro preguntas de la rúbrica se encuentran en `RESPUESTAS_RUBRICA.md`.
