from django.contrib import admin
from .models import Aluno, Cidade, Curso

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Cidade)
admin.site.register(Curso)
