from django.contrib import admin
from.models import Tarefa

# Register your models here.

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'estado')
