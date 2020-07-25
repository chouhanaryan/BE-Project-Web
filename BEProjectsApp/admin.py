from django.contrib import admin
from .models import Teacher, Project, Contributor

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Project)
admin.site.register(Contributor)
