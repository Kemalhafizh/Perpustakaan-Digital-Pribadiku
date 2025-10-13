from django import forms
from .models import Book, Profile, Genre
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    # Field untuk memilih genre dengan checkbox
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'cover_image', 
                  'synopsis', 'rating', 'genres']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Judul Light Novel',
            'author': 'Penulis / Author',
            'published_date': 'Tanggal Terbit',
            'cover_image': 'Gambar Sampul (Cover Image)',
            'synopsis': 'Sinopsis',
            'rating': 'Rating (1-5)',
            'genres': 'Pilih Genre',
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']