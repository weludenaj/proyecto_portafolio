# Generated by Django 4.1.3 on 2022-12-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(max_length=150, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tittle',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion'),
        ),
    ]
