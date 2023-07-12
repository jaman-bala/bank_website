from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Create, Organizations, Sector, Region



@admin.register(Create)
class CreateAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'city',
        'phone',
        'created',
    )
    list_filter = (
        'created',
    )
    search_fields = (
        'first_name',
        'last_name',
        'phone',
    )



@admin.register(Organizations)
class OreganizationsAdmin(admin.ModelAdmin):
    list_display = (
        'text_name',
    )

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = (
        'title_name',
    )

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'region_name',
    )