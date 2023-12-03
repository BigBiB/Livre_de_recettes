from django import forms
from django.forms import Form, CharField, ModelForm
from .models import BlogRecettes


class RecetteSearchForm(Form):
    recette = CharField(max_length=100, required=False)
    # ingredient = CharField(max_length=100, required=False)


class AddRecetteForm(forms.ModelForm):
    class Meta:
        model = BlogRecettes
        fields = ('name', 'ingredient', 'recipe', 'note', 'category', 'picture', 'url_picture', 'url_recipe',)
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control-lg'}),
            'ingredient': forms.TextInput(attrs={'class': 'form-control-lg'}),
            'recipe': forms.Textarea(attrs={'class': 'form-control-lg'}),
            'note': forms.Textarea(attrs={'class': 'form-control-lg'}),
            'category': forms.Select(attrs={'class': 'form-control-lg'}),
            'picture': forms.TextInput(attrs={'class': 'form-control-lg'}),
            'url_picture': forms.TextInput(attrs={'class': 'form-control-lg'}),
            'url_recipe': forms.TextInput(attrs={'class': 'form-control-lg'}),
        }