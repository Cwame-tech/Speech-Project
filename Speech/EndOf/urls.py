from django.urls import path
from .views import (
    PostListView,
    UserPostListView
)

from . import views


urlpatterns = [
    path('',views.index, name = 'index'),
    path('user/<str:username>',UserPostListView.as_view(), name = 'speech-posts'),
    path('speech/', PostListView.as_view(), name = 'speech'),
    path('about/', views.about, name = 'EndOf-about'),
    path('about/', views.about, name = 'EndOf-about'),
    path('speaker/',views.Speakview, name = 'speaker_detail'),
]