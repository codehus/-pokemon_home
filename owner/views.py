from django.shortcuts import render
from django.http import HttpResponse
from owner.models import Owner
# Create your views here.
def owner_list(request):
    #name = 'Hola Mundo'
    data = {
        'nombre' : 'Hussein Palomino',
        'edad': 25,
        'pais_nacimiento': 'Perú',
        'dni': '12345678',
        'vigente': False,
    },
    lista = [
        {
            'nombre': 'Hussein Palomino',
            'edad': 25,
            'pais_nacimiento': 'Perú',
            'dni': '12345678',
            'vigente': False,
        },
        {
            'nombre': 'Natalia Rodriguez',
            'edad': 22,
            'pais_nacimiento': 'Perú',
            'dni': '2564585',
            'vigente': False,
        },
        {
            'nombre': 'Roxana Huaman',
            'edad': 28,
            'pais_nacimiento': 'Perú',
            'dni': '54785855',
            'vigente': True,
        },
    ],

    data_context = {
        'nombre' : 'Juan Paredes',
        'edad' : 22,
        'pais' : 'Perú'
    },
    owners = Owner.objects.all()
    #return HttpResponse(name)
    return render(request, 'owner/owner_list.html', context={'data': owners})
