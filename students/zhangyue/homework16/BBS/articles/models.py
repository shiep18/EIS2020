from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()
    annex = models.FileField(upload_to='file/%Y%m%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('articles:article_detail', args=[self.id])

    class Meta:
        ordering = ('-created',)
