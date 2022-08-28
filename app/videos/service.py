import requests

from apikeys.models import ApiKey

from app.settings import SEARCH_API, SEARCH_QUERY, MAX_RESULTS

from datetime import datetime,  timedelta


# def fetch_videos():
#     print('Fetching videos...')
#     try:
#         # API_KEY = ApiKey.objects.filter(is_limit_over=False).first()
#         # if not API_KEY:
#         #     return {'error': 'All API Key Expired'}
#         # print('API_KEY', str(API_KEY.api_key))
#         # res = requests.get(SEARCH_API, params={
#         #     'key': 'AIzaSyD2KdotL_qjoGfWMNs_uBtlcbrxadyskr4',
#         #     # 'key': API_KEY.api_key,
#         #     'part': 'snippet',
#         #     'q': SEARCH_QUERY,
#         #     'maxResults': int(MAX_RESULTS),
#         #     'type': 'video',
#         #     'order': 'date',
#         #     'publishedAfter': '2019-01-01T00:00:00Z',
#         #     'publishedBefore': '2020-01-01T00:00:00Z'
#         # })
#         res = requests.get('https://www.googleapis.com/youtube/v3/search', params={
#             'key': 'AIzaSyD2KdotL_qjoGfWMNs_uBtlcbrxadyskr4',
#             'part': 'snippet',
#             'q': 'Attack',
#             'maxResults': 10,
#             'type': 'video',
#             'order': 'date',
#             'publishedAfter': '2019-01-01T00:00:00Z',
#             'publishedBefore': '2020-01-01T00:00:00Z'
#         })
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

def fetch_videos():
    res = requests.get(SEARCH_API, params={
        'key': 'AIzaSyD2KdotL_qjoGfWMNs_uBtlcbrxadyskr4',
        'part': 'snippet',
        'q': 'Movies',
        'maxResults': 15,
        'type': 'video',
        'order': 'date',
        'publishedAfter': (datetime.utcnow() - timedelta(minutes=5)).isoformat() + "Z",
        'publishedBefore': (datetime.utcnow()).isoformat() + "Z"
    })
    print('res', res.json())
    if res.status_code == 200:
        return res.json()
    return {'items': []}
