from django.contrib import admin
from .models import Section, Workout


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


@admin.register(Workout)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'section')
    list_display_links = ('user',)
    fieldsets = (
        (None, {'fields': ('user', 'section')}),
        ("Основная информация", {'fields': ('date', 'start_time', 'end_time')}),
    )
