from django.contrib import admin

# Register your models here.
from .models import Course, Skill


class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register([Course, Skill], AboutAdmin)