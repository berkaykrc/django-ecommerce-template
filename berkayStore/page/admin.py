from django.contrib import admin
from .models import Page, Carousel


class PageAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "pk",
        "title",
        "status",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "status",
    )

    list_editable = (
        "title",
        "status",
    )


admin.site.register(Page, PageAdmin)
admin.site.register(Carousel)
