from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Aluno
        fields = ['id','nome','cpf','rg','data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Matricula
        exclude=[]

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta: 
        model = Matricula
        fields = ['curso' , 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosCursoSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    class Meta: 
        model = Matricula
        fields = ['aluno']
