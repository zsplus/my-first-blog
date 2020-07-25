from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from mdeditor.fields import MDTextFormField
from django import forms
from django.views.generic import View
from .models import Post
from .models import Blog
from .forms import PostForm
import markdown

def blog_list(request):
	blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request , pk):
	blog = get_object_or_404(Blog , pk=pk)
	blog.text = markdown.markdown(blog.text,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
	return render(request, 'blog/blog_detail.html', {'blog': blog})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
	post = get_object_or_404(Post , pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
