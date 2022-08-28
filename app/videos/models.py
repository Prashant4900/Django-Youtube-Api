from django.db import models


# Create your models here.


class Videos(models.Model):
    """
    Model for Videos
    """
    videoId = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.URLField()
    publishedAt = models.DateTimeField()
    channelId = models.CharField(max_length=255)
    videoUrl = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishedAt']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
