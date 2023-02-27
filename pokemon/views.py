from django.shortcuts import render
from django.http import HttpResponse
from pokemon.models import Pokemon

# Create your views here.
def pokemon_list(request):
    #name = 'App Pokemon funcionando correctamente!!!'
    #return HttpResponse(name)
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/pokemon_list.html', context={'data': pokemon})

