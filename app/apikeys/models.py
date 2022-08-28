from django.db import models

# Create your models here.


class ApiKey(models.Model):
    """
    Model for API Keys
    """
    name = models.CharField(max_length=255, unique=True)
    api_key = models.CharField(max_length=255, unique=True)
    is_limit_over = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.is_limit_over}'

    def __repr__(self):
        return f'Name: {self.name} ,Is Limit: {self.is_limit_over}'

    class Meta:
        verbose_name = 'API Key'
        verbose_name_plural = 'API Keys'
