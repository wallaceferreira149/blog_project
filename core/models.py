from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length = 250, null = True)
    title = models.CharField(max_length = 250)
    post_text = models.TextField()
    is_active = models.BooleanField(default = True)
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_on']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author_comment = models.CharField(max_length = 250, null=True)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ['-created_at']
