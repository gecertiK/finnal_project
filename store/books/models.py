from django.db import models
from django.urls import reverse
import uuid


BOOK_ITEM_STATUS = (
    ('Available', 'Available'),
    ('Unavailable', 'Unavailable'),
)


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID"
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter description of the book")
    genre = models.ManyToManyField(Genre, help_text="Select a genre")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    pages = models.IntegerField()
    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookItem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200, help_text='Write place where book was placed', null=True)
    status = models.CharField(
        choices=BOOK_ITEM_STATUS,
        max_length=100,
        help_text='Status of book',
        default='Available'
    )

    class Meta:
        ordering = ['status']

    def __str__(self):
        return '%s, Status: %s' % (self.book.title, self.status)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
