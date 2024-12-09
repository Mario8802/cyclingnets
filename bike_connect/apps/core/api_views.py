from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import News
from .serializers import NewsSerializer


class NewsListAPI(ListAPIView):
    queryset = News.objects.filter(is_published=True).order_by('-created_at')
    serializer_class = NewsSerializer


class NewsDetailAPI(RetrieveAPIView):
    queryset = News.objects.filter(is_published=True)
    serializer_class = NewsSerializer
