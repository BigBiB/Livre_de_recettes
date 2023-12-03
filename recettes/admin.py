from django.contrib import admin

# Register your models here.
from .models import BlogRecettes, Category


# admin.site.register(BlogRecettes)
@admin.register(BlogRecettes)
class BlogRecettesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        # "slug",
        "author",
    )
    empty_value_display = "Inconnu"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        # "slug",
    )
