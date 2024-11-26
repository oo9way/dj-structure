from rest_framework import serializers
from apps.books.models import Book, BookReview
from apps.sales.models import OrderItem
from django.db.models import Sum

class BookReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.first_name")

    class Meta:
        model = BookReview
        fields = ("rate", "comment", "user")


class BookListModelSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.full_name")
    sold = serializers.SerializerMethodField()
    book_reviews = BookReviewSerializer(source="reviews", many=True)
    
    class Meta:
        model = Book
        fields = ("title", "cover", "price", "author", "sold", "book_reviews",)

    def get_sold(self, obj):
        # return obj.sold
        sold = 0
        for item in obj.orders.all():
            sold += item.qty

        return sold
    
    # aggregate
    # annotate