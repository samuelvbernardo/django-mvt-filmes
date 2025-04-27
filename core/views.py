from django.shortcuts import render
from .models import Filme

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/listafilmes.html', {'filmes': filmes})
