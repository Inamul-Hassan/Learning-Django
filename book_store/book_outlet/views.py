from django.shortcuts import render, get_object_or_404
from django.http import Http404
from book_outlet.models import Book
from django.db.models import Avg

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('title')
    number_of__books = books.count()
    average_rating = books.aggregate(Avg('rating'))
    # Book.objects.filter(title__endswith='us').update(title='It Ends With Us')
    # Book.objects.filter(title="Harry Potter").update(rating=4)
    return render(request, 'book_outlet/index.html', {'books': books,
                                                      'num_of_books': number_of__books, 'average_rating': average_rating})


def detailed(request, slug):
    # try:
    #     book = Book.objects.get(id=id)
    # except:
    #     Http404('Book not found')
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/detailed.html',
                  {'title': book.title,
                   'rating': book.rating,
                   'author': book.author,
                   'is_bestseller': book.is_bestseller})
