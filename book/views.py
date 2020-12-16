from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views import generic

# from .forms import BookEditForm
from .models import Book


def list_book(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)

    page = request.GET.get('page', 1)
    books = paginator.page(page)

    return TemplateResponse(request, 'book/index.html', {'books': books})


def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'book/book_detail.html', {'book': book})


"""
def record_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'book/record_book.html', {'book': book})


def book_edit(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('book:record_book', args=(book.id,)))

    else:
        form = BookEditForm(instance=book)
    return TemplateResponse(request, 'book/book_edit.html', {'form': form, 'book': book})
"""


def book_delete(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        book.delete()
        return HttpResponseRedirect(reverse('book:book_list'))
    else:
        return TemplateResponse(request, 'book/book_delete.html', {'book': book})


def like(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404
    book.like += 1
    book.save()
    return redirect('/book/')


def api_like(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404
    book.like += 1
    book.save()
    return JsonResponse({"like": book.like})


class Book_Add(generic.edit.CreateView):
    model = Book
    fields = '__all__'


class Book_Update(generic.edit.UpdateView):
    model = Book
    fields = '__all__'
