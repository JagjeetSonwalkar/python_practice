from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Blog
from .forms import BlogForm

# class based view

# CREATE
class BlogCreateView(View):
    def get(self, request):
        form = BlogForm()
        return render(request, "blogapp_cbv/blog_create.html", {"form": form})

    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
        return render(request, "blogapp_cbv/blog_create.html", {"form": form})

# LIST
class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, "blogapp_cbv/blog_list.html", {"blogs": blogs})

# DETAIL
class BlogDetailView(View):
    def get(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        return render(request, "blogapp_cbv/blog_detail.html", {"blog": blog})

# UPDATE
class BlogUpdateView(View):
    def get(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        form = BlogForm(instance=blog)
        return render(request, "blogapp_cbv/blog_update.html", {"form": form})

    def post(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
        return render(request, "blogapp_cbv/blog_update.html", {"form": form})

# DELETE
class BlogDeleteView(View):
    def get(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        return render(request, "blogapp_cbv/blog_delete.html", {"blog": blog})

    def post(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        blog.delete()
        return redirect("blog_list")