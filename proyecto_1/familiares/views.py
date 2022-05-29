from multiprocessing import context
from django.shortcuts import render
from familiares.models import familiares
# Create your views here.
def familiares(request):
    nuevo_familiar = familiares.objects.create(
        nombre ="Maria",
        edad = 27)
    context = {"nuevo_familiar": nuevo_familiar}
    return render(request, "familiares.html", context =  context)