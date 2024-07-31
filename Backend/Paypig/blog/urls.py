from django.urls import path
from .views import ContactView,EarnerView,PlaylistView,PlayListVideoView,PlaylistDestroyAPIView
# ,VideoUploadView,VideoDetailView,AddVideoView
urlpatterns =[

    path("message/",ContactView.as_view()),
    path("message/<uuid:pk>/",ContactView.as_view()),
    path("images/",EarnerView.as_view()),
    path("images/<uuid:pk>/",EarnerView.as_view()),
    path("playlist/",PlaylistView.as_view()),
    path("playlist/add/",PlaylistView.as_view()),
    path("playlist/delete/<uuid:pk>/",PlaylistDestroyAPIView.as_view()),
    path("playlist/<uuid:pk>/videos/",PlayListVideoView.as_view())
]