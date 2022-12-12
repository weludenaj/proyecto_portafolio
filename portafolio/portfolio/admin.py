from django.contrib import admin

from .models import Project
# Register your models here.
# Necesario para poder ver los campos ocultos
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)