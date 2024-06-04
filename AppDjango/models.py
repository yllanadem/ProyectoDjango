from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    grupo=models.IntegerField()

class Alumno(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fechaEntrega=models.DateField()
    entregado=models.BooleanField()