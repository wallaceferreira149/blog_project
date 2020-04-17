from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 250)
    post_text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_on']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ['-created_at']
