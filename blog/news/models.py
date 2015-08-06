# -*- coding: utf-8 -*-
from django.db import models


class Image(models.Model):
    title = models.CharField('Tytuł', max_length=255)
    slug = models.SlugField('Odnośnik', max_length=255, unique=True)
    description = models.TextField('Opis', blank=True, null=True)
    image = models.ImageField('Obrazek', upload_to="blog/static/pictures/")
    date = models.DateField('Data wykonania zdjęcia')


    class Meta:
        ordering = ["title"]
        verbose_name = "Obrazek"
        verbose_name_plural = "Obrazki"

    def __unicode__(self):
        return self.image.name

class News(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField('Tytuł', max_length=255)
    slug = models.SlugField('Odnośnik', max_length=255, unique=True)
    picture = models.ImageField('Zdjęcie', upload_to='blog/static/pictures/', blank=True)
    text = models.TextField(verbose_name='Treść')
    pictures = models.ManyToManyField(Image, verbose_name='Zdjęcia')
    posted_date = models.DateField('Data dodania')

    class Meta:
        verbose_name = "Wiadomość"
        verbose_name_plural = "Wiadomości"

    def __unicode__(self):
        return self.title


class NoteToPost(models.Model):
    post_id=models.ForeignKey(News)
    text = models.TextField(verbose_name='Tekst komentarza')
    posted_date = models.DateTimeField('Data dodania', auto_now_add=True)
    author = models.CharField('Autor', max_length=50)

    class Meta:
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"

