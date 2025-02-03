from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='services', null=True, verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Servicios"
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]