from django.urls import path

# from .views import liste, recette, categories, voir_recettes_par_categories
from .views import ListRecettes, categories
urlpatterns = [
    path('', ListRecettes.as_view(), name="recettes-index"),
    path('rec/cat/', categories, name="recettes-categories"),
    # path('cat,<str:numero_categorie>/', voir_recettes_par_categories, name="voir_recettes_par_categories"),
    # path('rec,<str:slug>,<int:cat_id>/', recette, name="recette"),
    # path('rec,<str:slug>,<str:numero_categorie>/', recette, name="recette"),
]
