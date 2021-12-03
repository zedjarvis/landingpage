from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.subject


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_post')
    updtated_on = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(default='blog.png',
                                   upload_to='media/',
                                   null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": str(self.slug)})
