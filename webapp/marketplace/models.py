from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField('Post title', max_length=100, null=False, blank=False)
    excerpt = models.CharField('Post excerpt', max_length=250, null=False, blank=False)
    body = models.TextField('Post body', null=False, blank=True)
    published_at = models.DateField('Post published at', null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/marketplace/{self.id}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'