from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone

class PostManager(models.Manager):
    def get_all_active(self):
        return super().get_queryset().filter(draft=False)

    def get_all_published(self):
        return super().get_queryset().filter(created__lte=timezone.now())

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    Body = models.TextField() 
    draft = models.BooleanField(default=False) 
    active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
   
    objects = PostManager()
   
    def __str__(self):
        return self.title
   
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})
   
    class Meta:
        ordering = ('-created',)
        