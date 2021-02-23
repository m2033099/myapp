from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views import generic

from .models import Book
from .forms import BookEditForm


def list_book(request):
    books = Book.objects.all()
    # いいねや編集後に順番が変わらないように本を登録した順(id順)に並び替える
    books = Book.objects.order_by('id')

    # 10冊を超えたら次のページを作る
    paginator = Paginator(books, 8)

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

    # book_delete.htmlのformからデータが送られてきた時にそのデータを消す
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


def book_edit(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    # 本が存在しない時はエラーメッセージを表示する
    except Book.DoesNotExist:
        raise Http404

    # book_edit.htmlのformからデータが送られてきた時にそのデータを保存する
    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            # 編集後はHome画面に戻る
            return HttpResponseRedirect(reverse('book:book_list'))

    else:
        form = BookEditForm(instance=book)
    # book_edit.htmlを呼び出す
    return TemplateResponse(request, 'book/book_edit.html',
                            {'form': form, 'book': book})
