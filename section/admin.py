from django.contrib import admin
from .models import Section, Workout


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title',)
    list_filter = ('user',)
    list_display_links = ('title',)
    fieldsets = (
        (None, {'fields': ('title', 'user')}),
    )


@admin.register(Workout)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'section')
    list_display_links = ('user',)
    fieldsets = (
        (None, {'fields': ('user', 'section')}),
        ("Основная информация", {'fields': ('date', 'start_time', 'end_time')}),
    )
