from django.urls import path
from .views import tarefas
from . import views

urlpatterns = [
    path('adicionar_tarefa/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('', tarefas, name='tarefas'),
]
