from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(blank=True, default=False, null=True)
    pages = models.IntegerField()
    created = models.DateField(default=timezone.now, null=True, blank=True)
    count = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    store_book_id = models.CharField(max_length=50, null=True, help_text='Book id from store')

    def __str__(self):
        return self.title

    def status_book(self):
        if self.count < 1:
            return self.available is False
        else:
            return self.available is True

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])