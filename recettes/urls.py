from django.urls import path
# from .views import liste, recette, categories, voir_recettes_par_categories
from django.views.generic import DetailView

from .models import BlogRecettes
from .views import recettes_list, categories_list, liste_rapide, AddRecette
urlpatterns = [

    # path('', index, name="home"),
    path('', recettes_list, name="home"),

    path("r", recettes_list, name="recettes"),

    path("lr", liste_rapide, name="recettes_rapide"),

    path("r<int:pk>", DetailView.as_view(model=BlogRecettes, template_name="recettes/recette_detail.html"),
         name="recette_detail"),

    path("rc<cid>/", categories_list, name="categories"),

    # path("create", AddRecette.as_view(model=BlogRecettes, template_name="recettes/add_recette.html"), name="ajout_recette"),
    path("create", AddRecette, name="ajout_recette"),
    # path('', ListRecettes.as_view(), name="recettes-index"),
    # path('cat/', ListCategories, name="recettes-categories"),
    # path('cat/<cid>', ListParCategories, name="voir_recettes_par_categories"),
    # path('r<pk>/', DetailRecette.as_view(), name="detail-recette"),
    # path(r'^s=(\w+)/$', recette_search_view, name="recherche"),
    # path(r'^search/(\w+)/$', recette_search_view, name="recherche_recette"),

    # path('cat/<cid>/', ListParCategories.as_view(), name="voir_recettes_par_categories"),
    # path('rec,<str:slug>,<int:cat_id>/', recette, name="recette"),
    # path('rec,<str:slug>,<str:numero_categorie>/', recette, name="recette"),
]
