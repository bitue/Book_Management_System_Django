from dataclasses import fields
from django import forms 
from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =['id', 'book_name', 'author', 'category'] 
        