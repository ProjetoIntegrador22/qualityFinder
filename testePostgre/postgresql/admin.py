from django.contrib import admin
from postgresql import models

# Register your models here.

class VisualProvedor(admin.ModelAdmin):
    list_display = ('nome', 'apelido', 'cnpj',)

class VisualPlanos(admin.ModelAdmin):
    list_display = ('nome',)



admin.site.register(models.Provedor, VisualProvedor)
admin.site.register(models.Planos, VisualPlanos)
