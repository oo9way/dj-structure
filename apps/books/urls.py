from .api_endpoints import BookListAPIView, BookRetrieveAPIView
from django.urls import path


urlpatterns = [
    path("list/", BookListAPIView.as_view(), name="book-list"),
    path("details/<int:pk>/", BookRetrieveAPIView.as_view(), name="book-detail")
]
