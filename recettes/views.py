import random
from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RecetteSearchForm, AddRecetteForm
from .models import BlogRecettes, Category


@login_required
def accueil_page(request):
    # PAGE D'ACCUEIL DU SITE
    return render(request, "../livre_recettes/home.html", locals())


def categories_boutons():
    cate_list = Category.objects.all()
    return cate_list


@login_required
def index(request):
    selected = "home"
    return render(request, "livre_recettes/home.html", locals())


@login_required
def recettes_list(request):
    global page
    selected = "liste_recettes"
    rec_list = BlogRecettes.objects.all()
    cate_list = Category.objects.all()
    total = len(rec_list)

    if request.method == "POST":
        form1 = RecetteSearchForm(request.POST)
        if form1.is_valid():
            base_url = reverse('recettes')
            query_string = urlencode(form1.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form1 = RecetteSearchForm()
        recette_form = request.GET.get("recette", "")
        ingredient_form = request.GET.get("ingredient", "")
        if recette_form is not None:
            rec_list = rec_list.filter(Q(name__icontains=recette_form) | Q(recipe__icontains=recette_form))
            form1.fields['recette'].initial = recette_form
        if ingredient_form is not None:
            rec_list = rec_list.filter(ingredient__icontains=ingredient_form)
            # form.fields['ingredient'].initial = ingredient_form
    # Pagination : nombre d'éléments par page
    paginator = Paginator(rec_list.order_by('-id'), 18)

    try:
        page = request.GET.get('p')
        if not page:
            page = 1
        rec_list = paginator.page(page)
    except EmptyPage:
        rec_list = paginator.page(paginator.num_pages())
    # return render(request, "recettes/recettes_list.html", locals())

    return render(request, "recettes/liste.html", locals())


def liste_rapide(request):
    rec_list = BlogRecettes.objects.all()

    if request.method == "POST":
        form1 = RecetteSearchForm(request.POST)
        if form1.is_valid():
            base_url = reverse('recettes')
            query_string = urlencode(form1.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form1 = RecetteSearchForm()
        recette_form = request.GET.get("recette", "")
        ingredient_form = request.GET.get("ingredient", "")
        if recette_form is not None:
            rec_list = rec_list.filter(Q(name__icontains=recette_form) | Q(recipe__icontains=recette_form))
            form1.fields['recette'].initial = recette_form
        if ingredient_form is not None:
            rec_list = rec_list.filter(ingredient__icontains=ingredient_form)


    return render(request, "recettes/liste_rapide.html", locals())


def categories_list(request, cid):
    cate_list = Category.objects.all()
    cat_list = Category.objects.filter(id=cid)
    # rec_list = BlogRecettes.objects.all()
    rec_list = BlogRecettes.objects.all()

    global page
    selected = "liste_recettes"
    rec_list = BlogRecettes.objects.filter(category_id=cid)

    if request.method == "POST":
        form1 = RecetteSearchForm(request.POST)
        if form1.is_valid():
            base_url = reverse('recettes')
            query_string = urlencode(form1.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form1 = RecetteSearchForm()
        recette_form = request.GET.get("recette", "")
        ingredient_form = request.GET.get("ingredient", "")
        if recette_form is not None:
            rec_list = rec_list.filter(Q(name__icontains=recette_form) | Q(recipe__icontains=recette_form))
            form1.fields['recette'].initial = recette_form
        if ingredient_form is not None:
            rec_list = rec_list.filter(ingredient__icontains=ingredient_form)
            # form.fields['ingredient'].initial = ingredient_form
    # Pagination : nombre d'éléments par page
    paginator = Paginator(rec_list.order_by('-id'), 12)

    try:
        page = request.GET.get('p')
        if not page:
            page = 1
        rec_list = paginator.page(page)
    except EmptyPage:
        rec_list = paginator.page(paginator.num_pages())
    # return render(request, "recettes/recettes_list.html", locals())

    # return render(request, "recettes/liste.html", locals())

    return render(request, "recettes/categories.html", locals())


# class AddRecette(CreateView):
#     model = BlogRecettes
#     form_class = AddRecetteForm
#     template_name = 'recettes/add_recette.html'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

def AddRecette(request):
    form2 = AddRecetteForm(request.POST or None)
    if form2.is_valid():
        instance = form2.save(commit=False)
        instance.save()
        return HttpResponseRedirect("create")



    rec_list = BlogRecettes.objects.all()
    if request.method == "POST":
        form1 = RecetteSearchForm(request.POST)
        if form1.is_valid():
            base_url = reverse('recettes')
            query_string = urlencode(form1.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form1 = RecetteSearchForm()
        recette_form = request.GET.get("recette", "")
        ingredient_form = request.GET.get("ingredient", "")
        if recette_form is not None:
            rec_list = rec_list.filter(Q(name__icontains=recette_form) | Q(recipe__icontains=recette_form))
            form1.fields['recette'].initial = recette_form
        if ingredient_form is not None:
            rec_list = rec_list.filter(ingredient__icontains=ingredient_form)

    context = {
        "form2": form2,
        "form1": form1,
    }

    return render(request, "recettes/add_recette.html", context)
