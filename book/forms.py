from django import forms
from book.models import Book


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'category',
            'title',
            'author',
            'recommend_level',
            'recommend_context',

        )
