from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_active',)
    list_filter = ('is_superuser', 'is_staff', 'is_active',)
    list_display_links = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ("Основная информация", {'fields': ('first_name', 'last_name', 'email', 'balance')}),
        ("Доступ", {'fields': ('is_active', 'is_staff', 'is_superuser',), }),
        ("Дополнительная информация", {'fields': ('last_login', 'date_joined')}),
    )
