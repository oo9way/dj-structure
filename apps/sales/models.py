from django.db import models

class Order(models.Model):
    client = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



class OrderItem(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.PROTECT, related_name="orders")
    qty = models.IntegerField(default=0)
    order = models.ForeignKey("Order", on_delete=models.PROTECT)
