from django.contrib import admin
from django.urls import path
from incidencias import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.bienvenida, name="bienvenida"),
]

# Vista personalizada para errores 404.
handler404 = "incidencias.views.error_404"
