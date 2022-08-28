import requests
from app.settings import API_KEY
from datetime import datetime,  timedelta

SEARCH_API = 'https://www.googleapis.com/youtube/v3/search'


def fetch_videos():
    print('Fetching videos...')
    res = requests.get(SEARCH_API, params={
        'key': API_KEY,
        'part': 'snippet',
        'q': 'Attack',
        'maxResults': 15,
        'type': 'video',
        'order': 'date',
        'publishedAfter': (datetime.utcnow() - timedelta(minutes=5)).isoformat() + "Z",
        'publishedBefore': (datetime.utcnow()).isoformat() + "Z"
    })
    if res.status_code == 200:
        return res.json()
    return {'items': []}


# Testing the fetch_videos function

# def fetch_videos():
#     print('Fetching videos...')
#     try:
#         # API_KEY = ApiKey.objects.filter(is_limit_over=False).first()
#         # if not API_KEY:
#         #     return {'error': 'All API Key Expired'}
#         # print('API_KEY', str(API_KEY.api_key))
#         # res = requests.get(SEARCH_API, params={
#         #     'key': API_KEY.api_key,
#         #     'part': 'snippet',
#         #     'q': SEARCH_QUERY,
#         #     'maxResults': int(MAX_RESULTS),
#         #     'type': 'video',
#         #     'order': 'date',
#         #     'publishedAfter': '2019-01-01T00:00:00Z',
#         #     'publishedBefore': '2020-01-01T00:00:00Z'
#         # })
#         print('res', res.json())
#         if res.status_code == 200:
#             return res.json()
#         else:
#             # API_KEY.is_limit_over = True
#             # API_KEY.save()
#             return {'error': 'API Key Limit Over'}

#     except Exception as e:
#         print('e', e)
#         return {'error': str(e)}
