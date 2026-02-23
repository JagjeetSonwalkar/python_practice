from django.shortcuts import render
from blog.models import Post
from django.db.models import Q

# Create your views here.
def post_list(request):
    query = request.GET.get('q')    # search keyword
    category = request.GET.get('category') # category filter

    posts = Post.objects.all()

    # search
    if query:
        posts = Post.filter(
            Q(title__icontains = query) |
            Q(title__icontains = query)
        )
    
    # filter by category
    if category:
        posts = posts.filter(catagory__iexact = category)

    return render(request, "blog/post_list.html", {"posts":posts, "query":query, "category":category})



