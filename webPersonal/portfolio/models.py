from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha Edición')
    link = models.URLField(verbose_name='Link', null=True, blank=True)
    
    class Meta:
        verbose_name='proyecto' #Permite renombrar el nombre a mostrar
        verbose_name_plural = 'proyectos'
        ordering = ['-created'] #Permite ordenar de mas nuevo

    def __str__(self):
        return self.title

