from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

from .models import Book, Author


class HomePageView(TemplateView):
    template_name = 'library/index.html'


class ProfilePageView(TemplateView):
    template_name = 'library/profile.html'


class BookListView(ListView):
    model = Book
    paginate_by = 10
    template_name = 'library/book_list.html'

    def post(self, request):
        object_list = Book.objects.filter(
            title__contains=request.POST.get('title'))

        return render(request,
                      self.template_name,
                      {'object_list': object_list})


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
