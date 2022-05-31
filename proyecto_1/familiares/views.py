from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.
def familiares(request):
    nuevo_familiar = Familiares.objects.create(
        nome ="Maria",
        edad = 27)
    
    context = {"nuevo_familiar": nuevo_familiar}
    
    return render(request, "template1.html", context)


def mostrar_familiares(request):
    consulta_db = Familiares.objects.all()
    
    return render(request, "template1.html", context = {"familiares":consulta_db})