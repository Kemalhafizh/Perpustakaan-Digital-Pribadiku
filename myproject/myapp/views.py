from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Profile, Genre
from .forms import BookForm, UserUpdateForm, ProfileUpdateForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator

# 1. VIEW HALAMAN UTAMA
@login_required
def home_view(request):
    # Mengambil semua parameter dari URL
    genre_filter = request.GET.get('genre')
    search_query = request.GET.get('q', '')
    sort_option = request.GET.get('sort', 'newest')

    # Mulai dengan buku milik pengguna yang login
    user_books = Book.objects.filter(user=request.user)

    # Terapkan filter genre
    if genre_filter:
        user_books = user_books.filter(genres__name=genre_filter)

    # Terapkan filter pencarian
    if search_query:
        user_books = user_books.filter(
            Q(title__icontains=search_query) | Q(author__icontains=search_query)
        )

    # Terapkan sorting berdasarkan pilihan
    if sort_option == 'title_asc':
        all_books = user_books.order_by('title')
    elif sort_option == 'title_desc':
        all_books = user_books.order_by('-title')
    elif sort_option == 'rating_desc':
        all_books = user_books.order_by('-rating', '-id')
    else: # Default sorting (newest)
        all_books = user_books.order_by('-id')
        
    # Logika Pagination
    paginator = Paginator(all_books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    all_genres = Genre.objects.all().order_by('name')

    context = {
        'page_obj': page_obj, 
        'search_query': search_query,
        'all_genres': all_genres,
        'current_sort': sort_option,
        'current_genre': genre_filter,
    }
    return render(request, 'myapp/index.html', context)

# 2. VIEW UNTUK MENAMBAH BUKU BARU
@login_required
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.user = request.user
            new_book.save()
            form.save_m2m() 
            return redirect('home')
    else:
        form = BookForm()
    
    context = {
        'form': form,
        'is_editing': False
    }
    return render(request, 'myapp/add_book.html', context)

# 3. VIEW UNTUK MELIHAT DETAIL BUKU
@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        return HttpResponseForbidden("Anda tidak memiliki izin untuk melihat halaman ini.")

    context = {
        'book': book
    }
    return render(request, 'myapp/book_detail.html', context)

# 4. VIEW UNTUK MENGEDIT BUKU
@login_required
def edit_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        return HttpResponseForbidden("Anda tidak memiliki izin untuk mengedit buku ini.")
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    
    context = {
        'form': form,
        'is_editing': True,
        'book': book
    }
    return render(request, 'myapp/add_book.html', context)

# 5. VIEW UNTUK MENGHAPUS BUKU
@login_required
def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        return HttpResponseForbidden("Anda tidak memiliki izin untuk menghapus buku ini.")
    
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    
    context = {
        'book': book
    }
    return render(request, 'myapp/delete_confirm.html', context)

# 6. VIEW UNTUK REGISTRASI PENGGUNA BARU
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'myapp/register.html', context)

# 7. VIEW UNTUK LOGIN PENGGUNA
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'myapp/login.html', context)

# 8. VIEW UNTUK LOGOUT PENGGUNA
def logout_view(request):
    logout(request)
    return redirect('home')

# 9. VIEW UNTUK PENGATURAN AKUN
@login_required
def account_settings_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                     request.FILES,
                                     instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Akun Anda telah berhasil diperbarui!')
            return redirect('account_settings')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'myapp/account_settings.html', context)
