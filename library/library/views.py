from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Book, Author


class HomePageView(TemplateView):
    template_name = 'library/index.html'


class BookListView(ListView):
    model = Book
    paginate_by = 10


class BookDetailView(DetailView):
    model = Book


class BookCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'books.can_add'
    model = Book
    fields = ['title', 'pages', 'authors', 'genres', 'publishers']


class AuthorListView(ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author
