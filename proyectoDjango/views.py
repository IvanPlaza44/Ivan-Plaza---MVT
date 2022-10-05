from contextvars import Context
from django.shortcuts import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from home.models import Familiar

# def hola(request):
#     return HttpResponse("<h1>Buenas clase</h1>")

# def nombre(request):
#     return HttpResponse("<h1>Mi nombre es Ivan</h1>")

# def fecha(request):
#     fecha_actual = datetime.now()
#     return HttpResponse(f"La fecha y hora actual es {fecha_actual}")

# def calcular_fecha_nacimiento(request, edad):
#     fecha = datetime.now().year - edad
#     return HttpResponse(f"Tu fecha de nacimiento aprox para tus {edad} años es {fecha}")

# def prueba_template(request):
      
#     mi_contexto = {    
#         "rango" : list(range(1,11)),
#         'valor_aleatorio': random.randrange(1,11)
#         }  
#     template = loader.get_template("prueba_template.html")
#     template_renderizado = template.render(mi_contexto)
#     return HttpResponse(template_renderizado)

def crear_familiar(request, nombre, apellido, nacionalidad):
    familiar = Familiar(nombre = nombre, apellido = apellido , nacionalidad = nacionalidad, edad = random.randrange(100), fecha_creacion = datetime.now())
    familiar.save()
    template = loader.get_template("crear_familiar.html")
    template_renderizado = template.render({'familiar': familiar})
    
    return HttpResponse(template_renderizado)

    
def ver_familiares(request):
    familiares = Familiar.objects.all()
    template = loader.get_template("ver_familiares.html")
    template_renderizado = template.render({'familiares': familiares})
    return HttpResponse(template_renderizado)