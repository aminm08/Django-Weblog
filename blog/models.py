from django.shortcuts import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )

    title = models.CharField(max_length=100)
    short_description = models.TextField(_('short description'))
    text = RichTextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blogs')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.id])


class Comment(models.Model):
    RATING_CHOICES = (
        ('1', _('Very bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    )
    body = models.TextField(_('Comment text '))
    rating = models.CharField(_('Your score '), choices=RATING_CHOICES, max_length=1)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    Blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    active = models.BooleanField(_('is thic comment active? '), default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}:{self.get_rating_display()}'

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.Blog.id])
