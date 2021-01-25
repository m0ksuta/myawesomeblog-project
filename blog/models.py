from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def get_summary(self):
        if len(self.text) > 70:
            return self.text[:70]+'...'
        else:
            return self.text

    def __str__(self):
        return self.title
