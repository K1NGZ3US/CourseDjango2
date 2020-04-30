from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Post


class HomeView(View):
    """Home page"""
    def get(self, request):
        post_list = Post.objects.all()
        return render(request, "blog/home.html", {"posts": post_list})


class CategoryView(View):
    """Displaying Category Articles"""
    def get(self, request, category_name):
        category = Category.objects.get(slug = category_name)
        return render(request, "blog/post_list.html", {"category": category})
    

class PostView(View):
    """Displaying Posts"""
    def get(self, request, post_id):
        post = Post.objects.get(slug = post_id)
        return render(request, "blog/post.html", {"post": post})