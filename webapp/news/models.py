from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField('Post title', max_length=100, null=False, blank=False)
    excerpt = models.CharField('Post excerpt', max_length=250, null=False, blank=False)
    body = models.TextField('Post body', null=False, blank=True)
    published_at = models.DateTimeField('Post published at', null=False, blank=False)

    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Newses'