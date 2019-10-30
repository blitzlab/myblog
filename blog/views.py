from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth import views

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_published__lte = timezone.now()).order_by('-date_published')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = PostForm
    model = Post
    redirect_field_name = 'blog/post_detail.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = PostForm
    redirect_field_name = 'blog/post_detail.html'
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_url = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_published__isnull = True).order_by('date_created')

# Comment Form Functions
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish()
    return redirect('blog:post_detail', pk=post.pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_comment.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)

@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail', post_pk)
