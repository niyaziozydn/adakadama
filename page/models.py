from django.db import models
from tinymce import models as tinymce_models



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True,verbose_name="Başlık")
    content = tinymce_models.HTMLField(verbose_name="İçerik")
    created_on = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    cover_image = models.ImageField(upload_to='post',verbose_name="İçerik Resmi")


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title    
