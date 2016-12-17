# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


# class Tag(models.Model):
#     title = models.CharField(max_length=100)
#     def __str__(self):
#         return self.title
#
#     def __unicode__(self):
#         return u'%s' % (self.title)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Article(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=500)
    body = RichTextField()
    slug = models.SlugField(max_length=500,unique_for_date='publish')
    image = models.ImageField(upload_to='images',null=True)
    tags = TaggableManager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    published = PublishedManager()

    # def get_absolute_url(self):
    #     return reverse('bet:post_detail',
    #                    args=[self.slug])
    def get_absolute_url(self):
        return reverse('bet:post_detail',
                       args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])

    def get_image_absolute_url(self):
        return 'http://127.0.0.1:8000'+self.image.url

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % (self.title)

class Prognostika(models.Model):
    kodikos = models.CharField(max_length=500)
    agonas = models.CharField(max_length=500)
    apodosi = models.CharField(max_length=500)
    simeio = models.CharField(max_length=500)
    apotelesma = models.CharField(max_length=500)
    bookmaker_link = models.CharField(max_length=500)
    bookmaker_title = models.CharField(max_length=500,null=True)
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    SPORTS = (
        ('football', 'Ποδόσφαιρο'),
        ('basketball', 'Μπάσκετ'),
        ('tennis', 'Τέννις'),
        ('volley', 'Βόλλευ'),
    )
    sport = models.CharField(max_length=10, choices=SPORTS, default='football')
    SIMEIA = (
        ('nulls', 'Κανένα'),
        ('success', 'Κερδισμένο'),
        ('danger', 'Χαμένο'),
    )
    xroma = models.CharField(max_length=10, choices=SIMEIA, default='nulls')


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.kodikos

    def __unicode__(self):
        return u'%s' % (self.kodikos)



class Block(models.Model):
    objects=models.Manager()
    CHOICES = [(i, i) for i in range(11)]
    SIDEBAR = (
        ('left', 'Left'),
        ('right', 'Right'),
        ('arxiki1', 'Αρχικη 1'),
        ('arxiki2', 'Αρχικη 2'),
        ('arxiki3', 'Αρχικη 3'),
        ('arxikipano', 'Αρχικη πανω'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=500)
    body = RichTextField()
    weight = models.IntegerField(choices=CHOICES)
    titleOn = models.BooleanField(default=True)
    sidebar = models.CharField(max_length=10, choices=SIDEBAR, default='right')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    published = PublishedManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:
        ordering = ('-weight',)


class Newsletter(models.Model):
    newsemail = models.EmailField(unique=True)
