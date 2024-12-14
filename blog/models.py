from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Creating Post model for our database
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Recognizing each individual post by their title in adminstration page
    def __str__(self):
        return self.title

    # Creating individual post URL by its primary key
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})