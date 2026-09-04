from datetime import datetime

from django.shortcuts import render


def bienvenida(request):
    """Renderiza la página principal con datos y una condición simple."""
    nombre = "Estudiante"
    cantidad_incidencias = 5
    incidencias_resueltas = 3
    incidencias_pendientes = cantidad_incidencias - incidencias_resueltas

    if incidencias_pendientes > 0:
        estado = "Existen incidencias pendientes de revisión."
    else:
        estado = "No existen incidencias pendientes."

    fecha_consulta = datetime.now().strftime("%d/%m/%Y %H:%M")

    contexto = {
        "nombre": nombre,
        "cantidad_incidencias": cantidad_incidencias,
        "incidencias_resueltas": incidencias_resueltas,
        "incidencias_pendientes": incidencias_pendientes,
        "estado": estado,
        "fecha_consulta": fecha_consulta,
    }

    return render(request, "bienvenida.html", contexto)


def error_404(request, exception):
    """Muestra una página personalizada cuando la URL no existe."""
    return render(request, "404.html", status=404)
