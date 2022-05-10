from unittest.util import _MAX_LENGTH
from django.db      import models
from django.urls    import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
    
