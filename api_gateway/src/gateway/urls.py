from django.urls import path, re_path
from .views import ProxyView

urlpatterns = [
    re_path(r'^api/(?P<service>[\w-]+)/(?P<path>.*)$', ProxyView.as_view(), name='proxy'),
]