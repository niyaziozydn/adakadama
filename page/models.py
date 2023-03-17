from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='post')


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title    
