from django import forms
from django.forms import ModelForm
from .models import Book

class formBook(ModelForm):

    class Meta:
        model = Book
        fields = "__all__"
        require_css_class = 'required-field'
        widgets = {
            'Fname': forms.TextInput(attrs={'placeholder': 'John','class':'wi50'}),
            'Lname': forms.TextInput(attrs={'placeholder': 'Williams'}),
            'date': forms.TextInput(attrs={'placeholder': '06/11/2023'}),
        }
        labels = {
            'Fname': 'First Name',
            'Lname': 'Last Name',
            'date': 'Date [mm/dd/yyyy]',
            'time': 'Time Slot'
        }