from django.contrib import admin
from .models import Dreamer

# Register your models here.

@admin.register(Dreamer)
class DreamerAdmin(admin.ModelAdmin):
    list_display = ['email', 'current_datetime', 'github_url']