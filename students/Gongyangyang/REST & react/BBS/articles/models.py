from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta: ordering = ('-pub_date',)

# from django.db import models 

# class Article(models.Model): 
#     title = models.CharField(max_length=50) 
#     body = models.TextField() 
#     created = models.DateTimeField(auto_now_add=True) 
#     updated = models.DateTimeField(auto_now=True) 

# class Meta: ordering = ('-created',)