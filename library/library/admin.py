from django.contrib import admin

from .models import Book, Author, Genre, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('authors',)
    list_display = ('title',)
    list_per_page = 15


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    list_per_page = 15


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    list_per_page = 15


@admin.register(Publisher)
class PPublisherAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    list_per_page = 15
