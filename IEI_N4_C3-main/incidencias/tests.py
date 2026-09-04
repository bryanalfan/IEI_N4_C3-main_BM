from django.test import TestCase
from django.urls import reverse


class BienvenidaViewTests(TestCase):
    def test_pagina_bienvenida_responde_correctamente(self):
        response = self.client.get(reverse("bienvenida"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bienvenida.html")
        self.assertContains(response, "Estudiante")
        self.assertContains(response, "2")

    def test_pagina_404_personalizada(self):
        response = self.client.get("/ruta-que-no-existe/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
        self.assertContains(response, "Página no encontrada")
