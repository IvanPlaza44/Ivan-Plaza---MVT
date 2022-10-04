from contextvars import Context
from django.shortcuts import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
def hola(request):
    return HttpResponse("<h1>Buenas clase</h1>")

def nombre(request):
    return HttpResponse("<h1>Mi nombre es Ivan</h1>")

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"La fecha y hora actual es {fecha_actual}")

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f"Tu fecha de nacimiento aprox para tus {edad} años es {fecha}")

def prueba_template(request):
      
    mi_contexto = {    
        "rango" : list(range(1,11)),
        'valor_aleatorio': random.randrange(1,11)
        }  
    template = loader.get_template("prueba_template.html")
    template_renderizado = template.render(mi_contexto)
    return HttpResponse(template_renderizado)

def crear_familiar(request):
    return HttpResponse()

    
def ver_familiares(request):
    return HttpResponse()
