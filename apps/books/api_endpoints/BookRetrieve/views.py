from rest_framework.generics import RetrieveAPIView
from .serializers import BookRetrieveModelSerializer
from apps.books.models import Book


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookRetrieveModelSerializer
    