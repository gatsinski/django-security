"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import (HomePageView, BookListView, BookDetailView, BookCreateView,
                    AuthorListView, AuthorDetailView, ProfilePageView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='index'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/',
         AuthorDetailView.as_view(),
         name='author_detail'),
    path('accounts/profile/', ProfilePageView.as_view(), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]
