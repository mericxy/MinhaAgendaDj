from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.

def tarefas(request):
    tarefas = Tarefa.objects.all()
    context = {'tarefas': tarefas}
    return render(request, 'index.html', context)

def adicionar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas')  # Redirecione para a página principal ou outra página após salvar
    else:
        form = TarefaForm()
    return render(request, 'index.html', {'form': form})
