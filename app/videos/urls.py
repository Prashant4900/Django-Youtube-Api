from django.urls import path
from . import views


urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('api/videos/list/', views.VideoListView.as_view(), name='videos-list'),
]
