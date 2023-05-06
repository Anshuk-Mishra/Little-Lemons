from django import forms
from django.forms import ModelForm
from .models import Book

class formBook(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"