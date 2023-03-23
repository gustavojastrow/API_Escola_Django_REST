from rest_framework import viewsets,generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibir todos os alunos """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CursosViewSet(viewsets.ModelViewSet):
    """ Exibir todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class ListaAlunosCurso(generics.ListAPIView):
    """Listando alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    