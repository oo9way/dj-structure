import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.develop")


from faker import Faker
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image

# Assuming you have Django models properly set up
from apps.books.models import Author, Book

fake = Faker()

# Function to create a fake image
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

def run():
    # Adjust the number of entries as needed
    generate_authors(n=10)
    generate_books(n=50)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.develop")
    import django
    django.setup()
    run()
