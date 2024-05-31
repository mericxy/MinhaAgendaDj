from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.

def index(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'index.html', {'tarefas': tarefas})

@require_POST
def add_task(request):
    nome = request.POST.get('nome')
    categoria = request.POST.get('categoria')
    if nome and categoria:
        nova_tarefa = Tarefa(nome=nome, categoria=categoria)
        nova_tarefa.save()
    return redirect('index')

@require_POST
def delete_task(request):
    tarefa_id = request.GET.get('id')
    if tarefa_id:
        Tarefa.objects.filter(id=tarefa_id).delete()
    return redirect('index')

@require_POST
def toggle_task_status(request):
    tarefa_id = request.GET.get('id')
    if tarefa_id:
        tarefa = Tarefa.objects.get(id=tarefa_id)
        tarefa.estado = not tarefa.estado
        tarefa.save()
    return JsonResponse({'success': True})