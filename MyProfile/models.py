from django.db import models
# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.subject
