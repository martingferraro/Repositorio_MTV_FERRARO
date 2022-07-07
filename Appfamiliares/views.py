from django.http import HttpResponse
from django.shortcuts import render
from Appfamiliares import views
from Appfamiliares.models import Familiar
from Appfamiliares import models
from django.template import Context, context, Template

# Create your views here.


def padre(self):
    padre= Familiar (nombre= "Juan", apellido="Perez", edad= "70", fecha_nacimiento="1952-11-15")
    padre.save()
    texto= f"Familiar creado. Nombre: {padre.nombre}, Apellido: {padre.apellido}, Edad: {padre.edad}, Fecha de nacimiento: {padre.fecha_nacimiento} "
    return HttpResponse (texto)

def madre(self):
    madre= Familiar (nombre= "Ana", apellido="Sosa", edad= "60", fecha_nacimiento="1962-10-26")
    madre.save()
    texto= f"Familiar creado. Nombre: {madre.nombre}, Apellido: {madre.apellido}, Edad: {madre.edad}, Fecha de nacimiento: {madre.fecha_nacimiento} "
    return HttpResponse (texto)

def hermano(self):
    hermano= Familiar (nombre= "Andres", apellido="Perez", edad= "30", fecha_nacimiento="1992-02-10")
    hermano.save()
    texto= f"Familiar creado. Nombre: {hermano.nombre}, Apellido: {hermano.apellido}, Edad: {hermano.edad}, Fecha de nacimiento: {hermano.fecha_nacimiento}"
    return HttpResponse (texto)

def padre_template(self):
    mi_archivo= open ("C:/Users/Martin/Documents/PYTHON/MTV_FERRARO/Plantillas/template1.html")

    nombre1= "Juan"
    Apellido= "Perez"
    Edad= "70"
    fecha= "1952-11-15"

    diccionario= {"nombre": nombre1, "apellido": Apellido, "Edad": Edad, "fecha": fecha }

    plantilla= Template(mi_archivo.read())
    mi_archivo.close()

    contexto= Context(diccionario)

    documento=plantilla.render(contexto)
    return HttpResponse (documento)

def madre_template(self):
    mi_archivo= open ("C:/Users/Martin/Documents/PYTHON/MTV_FERRARO/Plantillas/template1.html")

    nombre1= "María"
    Apellido= "Sosa"
    Edad= "60"
    fecha= "1962-10-25"

    diccionario= {"nombre": nombre1, "apellido": Apellido, "Edad": Edad , "fecha": fecha }

    plantilla= Template(mi_archivo.read())
    mi_archivo.close()

    contexto= Context(diccionario)

    documento=plantilla.render(contexto)
    return HttpResponse (documento)

def hermano_template(self):
    mi_archivo= open ("C:/Users/Martin/Documents/PYTHON/MTV_FERRARO/Plantillas/template1.html")

    nombre1= "Andres"
    Apellido= "Ferraro"
    Edad= "30"
    fecha= "1992-05-15"

    diccionario= {"nombre": nombre1, "apellido": Apellido, "Edad": Edad , "fecha": fecha}

    plantilla= Template(mi_archivo.read())
    mi_archivo.close()

    contexto= Context(diccionario)

    documento=plantilla.render(contexto)
    return HttpResponse (documento)
    
