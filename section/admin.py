from django.contrib import admin
from .models import Section, Publication


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_active',)
    list_filter = ('is_active',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {'fields': ('title', 'slug')}),
        ("Основная информация", {'fields': ('description',)}),
        ("Отображение", {'fields': ('is_active', ), }),
    )


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_active',)
    list_filter = ('is_active',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {'fields': ('title', 'slug')}),
        ("Основная информация", {'fields': ('section', 'description', 'image')}),
        ("Отображение", {'fields': ('is_active', ), }),
    )
