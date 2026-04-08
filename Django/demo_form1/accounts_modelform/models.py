from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title