from rest_framework import serializers
from apps.books.models import Book


class BookListModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ("title", "cover", "price",)


