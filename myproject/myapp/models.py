from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """
    Model ini merepresentasikan sebuah buku di dalam perpustakaan.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# Fungsi ini akan dijalankan SETIAP KALI sebuah objek User dibuat
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Fungsi ini menyimpan profil setiap kali objek User disimpan
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()