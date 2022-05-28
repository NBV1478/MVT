from multiprocessing import context
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje =f"Hoy es hoy {fecha} !!"
    return HttpResponse(mensaje)

def familia(request):
    return HttpResponse("<h1> Hola, esta es mi familia </h1>")
def integrantes(request):
    mama = "Elena"
    hermano_1 = "Matias"
    hermano_2 = "Diego"
    edades = 67, 37, 34
    mensaje = f"Mi mamá se llama {mama},su edad es {edades[0]} y mis hermanos son {hermano_1}, su edad es {edades[1]} y {hermano_2}, su edad es {edades[2]}"
    return HttpResponse(mensaje)  

def template(request):
    return render(request, "template1.html", context = [])