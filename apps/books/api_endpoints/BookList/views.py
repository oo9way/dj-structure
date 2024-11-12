from rest_framework.generics import ListAPIView
from .serializers import BookListModelSerializer
from apps.books.models import Book
from rest_framework import permissions


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListModelSerializer
