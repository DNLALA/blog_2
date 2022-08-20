import email
from email.mime import image
from pyexpat import model
from tabnanny import verbose
from tkinter import ACTIVE
from turtle import title
from unicodedata import category, name
from venv import create
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    category = models.ForeignKey(
        Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-create_at',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create_at',)

    def __str__(self):
        return self.name
