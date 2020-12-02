from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post'
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_queryset(self,*args, **kwargs):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title','content']
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:   
            messages.warning(request,'Login to create post')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        form.instance.author = self.request.user
        messages.success(self.request,f'{self.request.user.username} created a post!')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title','content']
    
    def form_valid(self, form):
        messages.success(self.request, f"{self.request.user}'s post is updated")
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog-home')

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        messages.success(request,f"{post.author}'s post is deleted")
        return super().delete(request,*args,**kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
