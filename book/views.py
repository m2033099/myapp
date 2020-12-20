from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views import generic

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
    # 本が存在しない時はエラーメッセージを表示する
    except Book.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'book/book_detail.html', {'book': book})


def book_delete(request, book_id):
    try:
        book = Book.objects.get(id=book_id)

    # 本が存在しない時はエラーメッセージを表示する
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

    # 本が存在しない時はエラーメッセージを表示する
    except Book.DoesNotExist:
        raise Http404

    # この関数が呼び出された時にlikeに１を足して保存する
    book.like += 1
    book.save()
    return redirect('/book/')


class Book_Add(generic.edit.CreateView):
    model = Book
    fields = '__all__'


class Book_Update(generic.edit.UpdateView):
    model = Book
    fields = '__all__'
