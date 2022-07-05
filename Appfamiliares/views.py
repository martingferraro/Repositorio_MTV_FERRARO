from django.http import HttpResponse
from django.shortcuts import render
from Appfamiliares import views
from Appfamiliares.models import Familiar
from Appfamiliares import models
from django.template import Context, context, Template

# Create your views here.


def padre(self):
    padre= Familiar (nombre= "Juan", apellido="Perez", edad= "70")
    padre.save()
    texto= f"Familiar creado. Nombre: {padre.nombre}, Apellido: {padre.apellido}, Edad: {padre.edad} "
    return HttpResponse (texto)

def madre(self):
    madre= Familiar (nombre= "Ana", apellido="Sosa", edad= "60")
    madre.save()
    texto= f"Familiar creado. Nombre: {madre.nombre}, Apellido: {madre.apellido}, Edad: {madre.edad} "
    return HttpResponse (texto)

def hermano(self):
    hermano= Familiar (nombre= "Andres", apellido="Perez", edad= "30")
    hermano.save()
    texto= f"Familiar creado. Nombre: {hermano.nombre}, Apellido: {hermano.apellido}, Edad: {hermano.edad} "
    return HttpResponse (texto)

def padre_template(self):
    mi_archivo= open ("C:/Users/Martin/Documents/PYTHON/MTV_FERRARO/Plantillas/template1.html")

    nombre1= "Juan"
    Apellido= "Perez"
    Edad= "70"

    diccionario= {"nombre": nombre1, "apellido": Apellido, "Edad": Edad }

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

    diccionario= {"nombre": nombre1, "apellido": Apellido, "Edad": Edad }

    plantilla= Template(mi_archivo.read())
    mi_archivo.close()

    contexto= Context(diccionario)

    documento=plantilla.render(contexto)
    return HttpResponse (documento)

def hermano_template(self):
    mi_archivo= open ("C:/Users/Martin/Documents/PYTHON/MTV_FERRARO/Plantillas/template1.html")

    nombre1= "Andres"
    Apellido= "Ferraro"
    Edad= "40"

    diccionario= {"nombre": nombre1, "apellido": Apellido, "Edad": Edad }

    plantilla= Template(mi_archivo.read())
    mi_archivo.close()

    contexto= Context(diccionario)

    documento=plantilla.render(contexto)
    return HttpResponse (documento)
    
