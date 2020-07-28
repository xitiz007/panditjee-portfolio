from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    instances = Blog.objects.all()
    return render(request, 'blog/blog-page.html', {'instances' : instances})

def detail_blog(request, blog_id):
    instance = get_object_or_404(Blog, pk= blog_id)
    return render(request, 'blog/detail.html', {'instance': instance})


