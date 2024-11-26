from django.utils.translation import gettext as _
from django.db import models

class Author(models.Model):
    full_name = models.CharField(_("Full name"), max_length=255)
    bio = models.TextField(_("Bio"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Book(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    cover = models.ImageField(_("Cover"), upload_to="covers")
    
    author = models.ForeignKey(
        to="Author", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
        verbose_name=_("Author")
    )

    quantity = models.IntegerField(_("Quantity"), default=0)
    price = models.DecimalField(_("Price"), decimal_places=2, max_digits=12)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    @staticmethod
    def generate_fake():

        from faker import Faker
        from django.core.files.base import ContentFile
        from io import BytesIO
        from PIL import Image
        import random

        fake = Faker()

        def create_fake_image():
            image = Image.new("RGB", (200, 300), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            buffer = BytesIO()
            image.save(buffer, format="JPEG")
            buffer.seek(0)
            return ContentFile(buffer.read(), name=f"{fake.uuid4()}.jpg")

        def generate_authors(n=10):
            authors = []
            for _ in range(n):
                authors.append(Author(full_name=fake.name(), bio=fake.text()))
            Author.objects.bulk_create(authors)

        def generate_books(n=50):
            authors = list(Author.objects.all())
            books = []
            for _ in range(n):
                author = random.choice(authors) if authors else None
                book = Book(
                    title=fake.sentence(nb_words=5),
                    description=fake.text(max_nb_chars=500),
                    author=author,
                    quantity=random.randint(0, 100),
                    price=round(random.uniform(10.00, 500.00), 2)
                )
                book.cover.save(fake.uuid4(), create_fake_image(), save=False)
                books.append(book)
            Book.objects.bulk_create(books, batch_size=20)

        generate_authors(n=100)
        generate_books(n=500)


class BookReview(models.Model):
    book = models.ForeignKey("Book", on_delete=models.PROTECT, related_name="reviews")
    rate = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    @staticmethod
    def create_fake_book_reviews(n=50):
        from apps.users.models import User
        import random
        from faker import Faker

        fake = Faker()

        books = list(Book.objects.all())
        users = list(User.objects.filter(role=User.UserRole.USER))

        if not books:
            print("No books found. Add some books first.")
            return

        if not users:
            print("No users with role 'User' found. Add users first.")
            return

        # Generate book reviews
        for _ in range(n):
            book = random.choice(books)  # Select a random book
            user = random.choice(users)  # Select a random user

            review = BookReview.objects.create(
                book=book,
                rate=random.randint(1, 5),  # Random rating between 1 and 5
                review=fake.paragraph(nb_sentences=5),  # Random review text
                user=user,
            )
            print(f"Created review for book '{book.title}' by user '{user.username}'")