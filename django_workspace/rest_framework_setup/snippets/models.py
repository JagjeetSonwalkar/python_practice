from django.db import models

# Create your models here.
class Snippets(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICE, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="Friendly", max_length=100)

    class Meta:
        ordering = ["created"]