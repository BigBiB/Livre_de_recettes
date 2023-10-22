from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("<h1> Bonjour, ceci est un test de l'index </h1>")
    prenom = "J-P"
    nom = "ALBERT"
    date = datetime.today()
    return render(request, "livre_recettes/index.html", context={'date': date, 'prenom': prenom, 'nom': nom})
