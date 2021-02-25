from django.contrib import admin
from .models import Section, Workout, UserSection


class UserList(admin.StackedInline):
    model = UserSection
    fieldsets = ((None, {'fields': ('user',)}), )


@admin.register(UserSection)
class Test(admin.ModelAdmin):
    list_display = ("user", "section")


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    inlines = [UserList]
    list_display = ('id', 'user', 'title',)
    list_filter = ('user',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {'fields': ('title', 'user', 'slug',)}),
        ("Дополнительная информация", {"fields": ('description',)})
    )


@admin.register(Workout)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'section')
    list_display_links = ('user',)
    fieldsets = (
        (None, {'fields': ('user', 'section')}),
        ("Основная информация", {'fields': ('date', 'start_time', 'end_time')}),
    )
