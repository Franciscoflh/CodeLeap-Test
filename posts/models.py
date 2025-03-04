from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_datetime']

    def __str__(self):
        return self.title
