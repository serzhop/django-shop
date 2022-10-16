from unicodedata import name
from django.contrib import admin
from . models import Category, Product

@admin.register(Category)
class CategoryAdnin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'availible', 'created', 'updated']
    list_filter = ['availible', 'created', 'updated']
    list_editable = ['price', 'availible']
    prepopulated_fields = {'slug' : ('name',)}



