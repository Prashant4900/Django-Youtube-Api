from isodate import parse_datetime

from celery import shared_task
from .models import Videos
from .service import fetch_videos

from django.db import transaction
from app.settings import VIDEO_BASE_URL

from app.celery import app


# @app.task(name='add_videos_in_database')
@shared_task(name='add_videos_in_database')
def add_videos_in_database():
    '''
    Its Receive video data from fetch_videos and stored in Database.
    '''
    print("add_videos_in_database")
    with transaction.atomic():
        json = fetch_videos()

        for item in json['items']:
            instance = Videos.objects.create(
                title=item['snippet']['title'],
                description=item['snippet']['description'],
                publishedAt=parse_datetime(item['snippet']['publishedAt']),
                thumbnail=item['snippet']['thumbnails']['medium']['url'],
                videoId=item['id']['videoId'],
                videoUrl=VIDEO_BASE_URL + item['id']['videoId'],
                channelId=item['snippet']['channelId']
            )
            instance.save()
