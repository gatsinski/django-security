from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):
    title = models.CharField(_('Title'), max_length=254)
    pages = models.PositiveIntegerField(_('Pages'))
    authors = models.ManyToManyField('Author', related_name='books')
    genres = models.ManyToManyField('Genre', related_name='books')
    publishers = models.ForeignKey('Publisher',
                                   related_name='books',
                                   null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})


class Author(models.Model):
    name = models.CharField(_('Name'), max_length=254)
    publishers = models.ManyToManyField('Publisher', related_name='authors')

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(_('Name'), max_length=254)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(_('Name'), max_length=254)

    def __str__(self):
        return self.name
