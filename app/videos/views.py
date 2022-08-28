
from django.shortcuts import render
from django.views import View

from .models import Videos
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import filters

from .serializers import VideoSerializer


class DashboardView(View):
    def get(self, request):
        """
        Display all videos
        """
        try:
            items = Videos.objects.all()
            return render(request, 'dashboard.html', {'items': items})
        except Exception as e:
            return render(request, 'dashboard.html', {'error': str(e)})

    def post(self, request):
        """
        Search videos
        """
        try:
            search = request.POST.get('search')
            items = Videos.objects.filter(
                Q(title__icontains=search) | Q(description__icontains=search))
            return render(request, 'dashboard.html', {'items': items})
        except Exception as e:
            print('e', e)
            return render(request, 'dashboard.html', {'error': str(e)})


class VideoListView(generics.ListAPIView):
    """
    View to retrieve all the videos
    """
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        description = self.request.query_params.get('description', None)
        if title is not None:
            return Videos.objects.filter(title__icontains=title).order_by('-publishedAt')
        elif description is not None:
            return Videos.objects.filter(description__icontains=description).order_by('-publishedAt')
        elif title is not None and description is not None:
            return Videos.objects.filter(title__icontains=title, description__icontains=description).order_by('-publishedAt')
        else:
            return Videos.objects.order_by('-publishedAt')
