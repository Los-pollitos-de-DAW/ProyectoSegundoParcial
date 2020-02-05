from rest_framework import serializers
from repositorio.models import *
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rol
        fields=('id','idRol','nombreRol')
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('id','idUsuario','rol','nombreCliente','usuario','password','estado','correo')

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Noticia
        fields=('id','idNoticia','usuario','nombreNoticia','descrNoticia','creadoFecha')

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrera
        fields=('id','idCarrera','nombreCarrera')

class TerminoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Termino
        fields=('id','idTermino','nombreTermino')

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Materia
        fields=('id','idMateria','carrera','nombreMateria')

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registro
        fields=('id','idRegistro','termino','usuario','materia')

class DescargaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Descarga
        fields=('id','idDescarga','idRegistro','fecha')

