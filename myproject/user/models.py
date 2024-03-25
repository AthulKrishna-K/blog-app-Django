from django.db import models

from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=timezone.now)  # Set default value to current date
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


