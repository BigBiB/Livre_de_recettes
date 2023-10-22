# from django.db.models import Prefetch
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import BlogRecettes, Category
from django.core.exceptions import ObjectDoesNotExist


# def liste(request):
#     liste_recettes = BlogRecettes.objects.all()
#     liste_cat = Category.objects.all()
#     return render(request, f"recettes/body.html", context={"liste_recettes": liste_recettes, "liste_cat": liste_cat})
def accueil_page(request):
    return render(request, "../livre_recettes/index.html")


def get_queryset():
    return BlogRecettes.objects.all()


class ListRecettes(generic.ListView):
    model = BlogRecettes
    context_object_name = "recette_liste"
    template_name = "recettes/_index.html"


def categories(request):
    liste_cat = Category.objects.all()
    liste_recettes = BlogRecettes.objects.all()
    return render(request, f"recettes/categories.html",
                  context={"liste_cat": liste_cat, "liste_recettes": liste_recettes})

#
# def voir_recettes_par_categories(request, numero_categorie):
#     ma_categorie = Category.objects.get(pk=numero_categorie)
#     mes_recettes = BlogRecettes.objects.filter(category_id=ma_categorie)
#     cat_id = numero_categorie
#     print(request, "   ", numero_categorie, ma_categorie)
#     return render(request, f"recettes/recettes_par_categories.html",
#                   context={"ma_categorie": ma_categorie, "mes_recettes": mes_recettes, "cat_id": cat_id})
#
#
# def recette(request, slug, cat_id):
#     try:
#         rec = BlogRecettes.objects.get(slug=slug)
#         rid = rec.id
#         rnom = rec.nom
#         rrecette = rec.recette
#         rimage = rec.image
#         categ = Category.objects.filter(pk=cat_id)
#         for c in categ:
#             categ = c
#
#             try:
#                 categ=cat_id
#                 return render(request, f"recettes/recette.html",
#                           context={"recette": rec, "rid": rid, "rnom": rnom, "rrecette": rrecette, "rimage": rimage,
#                                    "rcat": categ})
#             except ObjectDoesNotExist:
#                 return render(request, f"recettes/recette_not_found.html")
#
#     except ObjectDoesNotExist:
#         return render(request, f"recettes/recette_not_found.html")
