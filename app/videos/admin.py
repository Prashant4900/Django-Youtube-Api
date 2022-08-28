from django.contrib import admin

from .models import Videos


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'publishedAt')
    list_filter = ('publishedAt',)
    search_fields = ('title', 'description')
    ordering = ['-publishedAt']
    list_per_page: int = 20
