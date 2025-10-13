from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL Inti & CRUD Buku
    path('', views.home_view, name='home'),
    path('tambah/', views.add_book_view, name='add_book'),
    path('book/<int:pk>/', views.book_detail_view, name='book_detail'),
    path('book/<int:pk>/edit/', views.edit_book_view, name='edit_book'),
    path('book/<int:pk>/hapus/', views.delete_book_view, name='delete_book'),
    
    # URL Autentikasi & Akun
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('akun/', views.account_settings_view, name='account_settings'),
    
    # URL Ganti Password
    path('akun/password/', 
         auth_views.PasswordChangeView.as_view(
             template_name='myapp/password_change.html',
             success_url=reverse_lazy('password_change_done')
         ), 
         name='password_change'),
    path('akun/password/sukses/', 
         auth_views.PasswordChangeDoneView.as_view(
             template_name='myapp/password_change_done.html'
         ), 
         name='password_change_done'),
         
    # URL Reset Password (Lupa Password)
    path('reset-password/', 
         auth_views.PasswordResetView.as_view(
             template_name='myapp/password_reset_form.html',
             email_template_name='myapp/password_reset_email.html',
             success_url=reverse_lazy('password_reset_done')
         ), 
         name='password_reset'),
    path('reset-password/terkirim/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='myapp/password_reset_done.html'
         ), 
         name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='myapp/password_reset_confirm.html',
             success_url=reverse_lazy('password_reset_complete')
         ), 
         name='password_reset_confirm'),
    path('reset-password/selesai/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='myapp/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
         
    # URL Filter Genre
    path('genre/<str:genre_name>/', views.genre_books_view, name='genre_books'),
]