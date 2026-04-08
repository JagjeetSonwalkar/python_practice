from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blogx
from .forms import BlogForm

# class based functions with gernerics
class BlogCreateView(CreateView):
    model = Blogx
    form_class = BlogForm
    template_name = "blogapp/blog_create.html"
    success_url = reverse_lazy('blog_list')

class BlogListView(ListView):
    model = Blogx
    template_name = "blogapp/blog_list.html"
    context_object_name = "blogs"

class BlogDetailView(DetailView):
    model = Blogx
    template_name = "blogapp/blog.html"
    context_object_name = "blog"

class BlogUpdateView(UpdateView):
    model = Blogx
    form_class = BlogForm
    template_name = "blogapp/blog_create.html"
    success_url = reverse_lazy("blog_list")

class BlogDeleteView(DeleteView):
    model = Blogx
    template_name = "blogapp/blog_delete.html"
    success_url = reverse_lazy("blog_list")