from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "pk",
        "title",
        "price",
        "stock",
        "cover_image",
        "status",
        "in_homepage",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "status",
        "price",
        "in_homepage",
    )

    list_editable = (
        "title",
        "status",
        "price",
        "in_homepage",
    )


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "pk",
        "title",
        "gender",
        "slug",
        "status",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "status",
        "gender",
    )

    list_editable = (
        "title",
        "status",
        "slug",
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
