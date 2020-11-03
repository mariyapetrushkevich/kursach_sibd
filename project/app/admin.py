from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Department)
admin.site.register(models.Speciality)
admin.site.register(models.Group)
admin.site.register(models.Student)
admin.site.register(models.Spravki)
admin.site.register(models.Discipline)
admin.site.register(models.Vedomost)

