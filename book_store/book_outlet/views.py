from django.shortcuts import render, get_object_or_404
from django.http import Http404
from book_outlet.models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()
    Book.objects.filter(title__endswith='us').update(title='It Ends With Us')
    return render(request, 'book_outlet/index.html', {'books': books})


def detailed(request, id):
    # try:
    #     book = Book.objects.get(id=id)
    # except:
    #     Http404('Book not found')
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_outlet/detailed.html',
                  {'title': book.title,
                   'rating': book.rating,
                   'author': book.author,
                   'is_bestseller': book.is_bestseller})
