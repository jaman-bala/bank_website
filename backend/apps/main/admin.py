from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Photo





@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
        "created",
        "img1",            
    )
    search_fields = (
        "title",     
    )
    list_filter = (
        "is_active",
        "created",
    )

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img1.url}" style="max-height: 330px;">')



