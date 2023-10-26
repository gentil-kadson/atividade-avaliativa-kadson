from django.urls import path
from .views import index, criar_aluno, editar_aluno, excluir_aluno

urlpatterns = [
    path('', index, name="home"),
    path('criar-aluno/', criar_aluno, name="criar_aluno"),
    path('editar-aluno/<int:id_aluno>/', editar_aluno, name="editar_aluno"),
    path('excluir-aluno/<int:id_aluno>/', excluir_aluno, name="excluir_aluno")
]