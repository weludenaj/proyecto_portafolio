from django.db import models

# Create your models here.

class Project (models.Model):
    tittle = models.CharField(max_length=200, verbose_name= 'Titulo')
    description= models.TextField(verbose_name= 'Descripcion')
    image= models.ImageField(upload_to='projects', verbose_name= 'Imagen')
    link= models.URLField(max_length=150, verbose_name= 'Enlace')
    created= models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')
    updated= models.DateTimeField(auto_now= True, verbose_name='Fecha Modificacion')

    # Pasos para convertir en español la aplicacion
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']
    
    # Para que muestre el titulo como link para acceder 
    def __str__(self):
        return self.tittle