from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=36)
    # slug = AutoSlugField(populate_from='name', unique=True, max_length=50)

    # slug = models.SlugField()

    def __str__(self):
        return self.name


class BlogRecettes(models.Model):
    name = models.CharField(max_length=100, blank=False)
    recipe = models.TextField(blank=False, null=True)
    ingredient = models.TextField(blank=False, null=True)
    note = models.TextField(blank=True, null=True)
    # slug = AutoSlugField(populate_from='name', unique=True, max_length=100)
    # tag = models.TextField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    picture = models.CharField(max_length=200, blank=True)
    url_picture = models.URLField(max_length=200, blank=True)
    url_recipe = models.URLField(max_length=200, blank=True)  # url vers recette  RECIPE = RECETTE
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Recette"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # if not self.slug:
        #     self.slug = slugify(self.name)

        super().save(*args, **kwargs)

