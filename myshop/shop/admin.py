from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Добавление модели категорий в админку."""
    list_display = ['name', 'slug']
    # Значение 'slug' будет браться от значения 'name'.
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Добавление модели товаров в админку."""
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    # list_editable позволяет редактировать поля,
    # находясь на странице отображения списка.
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
