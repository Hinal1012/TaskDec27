from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'color', 'created_by']
    list_display = ['name', 'color', 'created_by']

admin.site.register(Project, ProjectAdmin)