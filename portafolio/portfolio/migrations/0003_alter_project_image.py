# Generated by Django 4.1.3 on 2022-12-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_alter_project_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
    ]
