from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import uuid

class EmailSubscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class CategoryTypes(models.Model):
    types = models.CharField(max_length=30)
    
    class Meta:
        ordering = ('types',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.types


class Notice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='media', default='default.jpg', null=True, blank=True)
    category = models.ForeignKey(CategoryTypes, blank=False, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/documents', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(Notice, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
     
