from django.db import models

# Create your models here.

# Modelo para Formacion = Course


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    degree_tittle = models.CharField(max_length=300, verbose_name='Titulo Obtenido')
    description = models.TextField(verbose_name='Descripcion')
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')

    class Meta:
        verbose_name = 'Formacion'
        verbose_name_plural = 'Formaciones'
    # Para que muestre el titulo como link para acceder 
    def __str__(self):
        return self.title


# Modelo para Skill

class Skill(models.Model):
    title = models.CharField(max_length=80, verbose_name='Titulo')
    image = models.ImageField(upload_to='skills', verbose_name='Imagen')
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')

    class Meta:
        verbose_name = 'Conocimiento'
        verbose_name_plural = 'Conocimientos'
# Para que muestre el titulo como link para acceder 
    def __str__(self):
        return self.title