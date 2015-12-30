from django.db import models
from django.utils.translation import ugettext_lazy as _

import random
import string


def get_path(instance, filename):
  chars = string.ascii_letters + string.digits
  return "images/{}-{}".format(
    ''.join(random.sample(chars, 8)),
    filename.replace(')', '').replace('(', '')
  )


class Contact(models.Model):

  name = models.CharField(max_length=100)
  mail = models.EmailField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100, blank=True, null=True)


class Post(models.Model):

  title = models.CharField(_('Title'), max_length=100)
  slug = models.SlugField(_('Slug'), unique=True, max_length=255)
  type = models.CharField(_('Type'), max_length=4, choices=(
    ('text', _('Text')), ('tuto', _('Tutorial'))), default='text')

  published = models.BooleanField(_('Published'), default=True)
  created = models.DateTimeField(_('Created'), auto_now_add=True)
  publish_on = models.DateTimeField('Publish on', blank=True, null=True)

  class Meta:
    ordering = ['-publish_on']


class PostPart(models.Model):
  post = models.ForeignKey(Post, related_name='parts')
  type = models.CharField(_('Type'), max_length=5, choices=(
    ('nopic', _('No picture')),
    ('left', _('Picture on the left')),
    ('right', _('Picture on the right')),
    ('pic', _('One picture only'))),
    default='left'
  )
  pic = models.ImageField(_('Picture'), upload_to=get_path, blank=True, null=True)
  text = models.TextField(_('Text'), null=True, blank=True)
  ordernum = models.PositiveIntegerField()

  class Meta:
    ordering = ['ordernum']
