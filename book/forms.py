from django import forms
from book.models import Book


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'category',
            'title',
            'recommend_level',
            'recommend_context',

        )


class BookAdd(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'category',
            'title',
            'recommend_level',
            'recommend_context',
        )
