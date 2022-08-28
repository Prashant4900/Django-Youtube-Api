from django.contrib import admin
from .models import ApiKey

# Register your models here.


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ['name', 'api_key', 'is_limit_over',
                    'created_at', 'updated_at']
    list_filter = ['is_limit_over', ]
    search_fields = ['name', 'api_key']
    ordering = ['name']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('General', {'fields': ['name', 'api_key', 'is_limit_over', ]}),
        ('Metadata', {'fields': ['created_at', 'updated_at']})
    ]

    class Meta:
        verbose_name = 'API Key'
        verbose_name_plural = 'API Keys'
