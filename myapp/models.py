from django.db import models
from .utils import generate_random_token  # Ensure this function exists in utils.py

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'

class AuthToken(models.Model):
    key = models.CharField(max_length=64, unique=True, blank=True)  # allow blank for auto-generation
    label = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:  # Only generate a key if not provided
            self.key = generate_random_token(32)  # 32 bytes → 64 hex characters
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label or self.key
