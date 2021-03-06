# Generated by Django 3.0.3 on 2020-02-04 17:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('idCarrera', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCarrera', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('idMateria', models.AutoField(primary_key=True, serialize=False)),
                ('nombreMateria', models.CharField(max_length=500)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.AutoField(primary_key=True, serialize=False)),
                ('nombreRol', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Termino',
            fields=[
                ('idTermino', models.AutoField(primary_key=True, serialize=False)),
                ('nombreTermino', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=500)),
                ('usuario', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('estado', models.BooleanField()),
                ('correo', models.CharField(max_length=500)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.Rol')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('idRegistro', models.AutoField(primary_key=True, serialize=False)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.Materia')),
                ('termino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.Termino')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('idNoticia', models.AutoField(primary_key=True, serialize=False)),
                ('nombreNoticia', models.CharField(max_length=500)),
                ('descrNoticia', models.CharField(max_length=500)),
                ('creadoFecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Descarga',
            fields=[
                ('idDescarga', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('idRegistro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.Registro')),
            ],
        ),
    ]
