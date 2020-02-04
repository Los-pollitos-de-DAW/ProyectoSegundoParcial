from django.db import models
from django.utils import timezone
# Create your models here.
class Rol(models.Model):
    idRol=models.AutoField(primary_key=True)
    nombreRol=models.CharField(max_length=200)

class Usuario(models.Model):
    idUsuario=models.AutoField(primary_key=True)
    rol=models.ForeignKey(Rol,on_delete=models.CASCADE)
    nombreCliente= models.CharField(max_length=500)
    usuario=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    estado=models.BooleanField()
    correo=models.CharField(max_length=500)
class Noticia(models.Model):
    idNoticia=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nombreNoticia=models.CharField(max_length=500)
    descrNoticia=models.CharField(max_length=500)
    creadoFecha = models.DateTimeField(default=timezone.now)

class Carrera(models.Model):
    idCarrera=models.AutoField(primary_key=True)
    nombreCarrera=models.CharField(max_length=500)

class Termino(models.Model):
    idTermino=models.AutoField(primary_key=True)
    nombreTermino=models.CharField(max_length=500)

class Materia(models.Model):
    idMateria=models.AutoField(primary_key=True)
    carrera=models.ForeignKey(Carrera,on_delete=models.CASCADE)
    nombreMateria=models.CharField(max_length=500)

class Registro(models.Model):
    idRegistro=models.AutoField(primary_key=True)
    termino=models.ForeignKey(Termino,on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    materia=models.ForeignKey(Materia,on_delete=models.CASCADE)

class Descarga(models.Model):
    idDescarga=models.AutoField(primary_key=True)
    idRegistro = models.ForeignKey(Registro,on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title