from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Blog

# before saving the blog
@receiver(pre_save, sender = Blog)
def before_blog_save(sender, instance, **kwargs):
    print(f"About to save blog[Pre-Save]: {instance.title}")

# after saving the blog
@receiver(post_save, sender = Blog)
def before_blog_save(sender, instance, created, **kwargs):
    if created:
        print(f"new blog created[Post-Save]: {instance.title}")
    else:
        print(f"Blog updated[Post-Save]: {instance.title}")