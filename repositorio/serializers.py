from rest_framework import serializers
from repositorio.models import *
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rol
        fields=('idRol','nombreRol')
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('idUsuario','rol','nombreCliente','usuario','password','estado','correo')

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Noticia
        fields=('idNoticia','usuario','nombreNoticia','descrNoticia','creadoFecha')

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrera
        fields=('idCarrera','nombreCarrera')

class TerminoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Termino
        fields=('idTermino','nombreTermino')

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Materia
        fields=('idMateria','carrera','nombreMateria')

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registro
        fields=('idRegistro','termino','usuario','materia')

class DescargaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Descarga
        fields=('idDescarga','idRegistro','fecha')

