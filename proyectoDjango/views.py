from contextvars import Context
from django.shortcuts import HttpResponse
from datetime import datetime
from django.template import Context, Template
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

def mi_template(request):

    cargar_archivo = open(r'C:\Users\Ivan Plaza\Desktop\Proyecto Ivan\Proyecto Django\templates\template.html', 'r')
                             
    template = Template(cargar_archivo.read())
    
    cargar_archivo.close()
    
    contexto = Context()
       
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

