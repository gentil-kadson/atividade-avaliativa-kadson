from .forms import AlunoForm
from .models import Aluno
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    context = { 'alunos': alunos }

    return render(request, 'index.html', context)

def criar_aluno(request):
    aluno_form = AlunoForm()
    context = { 'form': aluno_form }

    if request.method == 'POST':
        aluno_form = AlunoForm(request.POST)
        if aluno_form.is_valid():
            aluno_form.save()
            return HttpResponseRedirect('/')

    return render(request, 'salvar_aluno.html', context)

def editar_aluno(request, id_aluno):
    aluno = Aluno.objects.get(id=id_aluno)
    aluno_form = AlunoForm(instance=aluno)

    if request.method == 'POST':
        aluno_form = AlunoForm(request.POST, instance=aluno_form)

        if aluno_form.is_valid():
            aluno_form.save()

            return HttpResponseRedirect('/')
    
    context = { 'form': aluno_form }
    return render(request, 'salvar_aluno.html', context)

def excluir_aluno(request, id_aluno):
    aluno = Aluno.objects.get(id=id_aluno)
    aluno.delete()
    return HttpResponseRedirect('/')