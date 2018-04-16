from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AuthorListView(ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('book_list')
    else:
        return render(request,
                      'registration/login.html',
                      {'form': AuthenticationForm})
