from rest_framework.generics import ListAPIView
from .serializers import BookListModelSerializer
from apps.books.models import Book, BookReview
from rest_framework import permissions
from apps.books.tasks import send_telegram_message
from django.db.models import Sum, Prefetch

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers


class BookListAPIView(ListAPIView):
    queryset = (Book.objects
                .select_related("author",)
                .prefetch_related(
                    Prefetch(
                        "reviews",
                        queryset=BookReview.objects.select_related("user")
                    )
                )
                .annotate(sold=Sum("orders__qty"))
                .only("title", "cover", "price", "author", "author__full_name",)
            )
                
    # queryset = Book.objects.all()
    serializer_class = BookListModelSerializer
    # pagination_class = None
    permission_classes = (permissions.AllowAny,)

    @method_decorator(cache_page(60 * 10))
    def get(self, request, *args, **kwargs):
        print("from query")
        return super().get(request, *args, **kwargs)