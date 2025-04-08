from django.urls import path
from .views import RegisterAPIView, LoginAPIView, HelloWorldAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('hi/', HelloWorldAPIView.as_view(), name='hello_world')
]