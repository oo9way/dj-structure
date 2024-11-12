from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import Book, Author



class BookAdmin(TranslationAdmin):
    list_display = ("title", "description")
    group_fieldsets = True


admin.site.register(Book, BookAdmin)
admin.site.register(Author)