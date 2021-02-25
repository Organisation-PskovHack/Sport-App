from django.contrib import admin
from .models import Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ("title", "key", "value")
