from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    filevideo = models.FileField(upload_to='projects', null=True, verbose_name='Archivo de vídeo')
    created =models.DateTimeField(auto_now_add=True, verbose_name='Fecha de carga')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')


    def __str__(self):
        return self.title

    class Meta:
        db_table = "Proyectos"
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]