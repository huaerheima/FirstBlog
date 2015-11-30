from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 
from .models import Blog, Comment
from .forms import BlogForm, CommentForm

def blog_list(request):
	blogs = Blog.objects.all()
	# for blog in blogs:
	# 	blog.text = blog.text[:500]
	return render(request,'blog_list.html',{'blogs':blogs})

def blog_detail(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	if request.method=="POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.blog = blog
			comment.save()
			return redirect('myblog.views.blog_detail', pk=pk)
	else:
		form = CommentForm()
	return render(request,'blog_detail.html',{'blog':blog,'form':form})