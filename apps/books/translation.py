from modeltranslation.translator import translator, TranslationOptions
from .models import Book


class BookTranslationOptions(TranslationOptions):
    fields = ("title", "description",)

# translator.register(Book, BookTranslationOptions)