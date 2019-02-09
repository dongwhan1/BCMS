from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Like, Map_Data
from .forms import PostForm, CommentForm, Suggest_Form, Map_Data_Form
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'bcms/home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'bcms/post_list.html', {'posts': posts})

def newsfeed1(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), board=1).order_by('-published_date')
    return render(request, 'bcms/newsfeed1.html', {'posts': posts})

def newsfeed2(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), board=2).order_by('-published_date')
    return render(request, 'bcms/newsfeed2.html', {'posts': posts})

def newsfeed3(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), board=3).order_by('-published_date')
    return render(request, 'bcms/newsfeed3.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'bcms/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'bcms/post_edit.html', {'form':form},)

@csrf_exempt
def newdata(request):
    if request.method == "POST":
        form = Map_Data_Form(request.POST)
        if form.is_valid():
            map_data = form.save(commit=False)
            map_data.loc_x = request.POST["loc_x"]
            map_data.loc_y = request.POST["loc_y"]
            map_data.save()
            return redirect('map/')
    return render(request, 'bcms/Map.html')


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'bcms/post_edit.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'bcms/add_comment_to_post.html', {'form':form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'bcms/post_draft_list.html', {'posts':posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def map(request):
    return render(request, 'bcms/Map.html')

@login_required # TODO: Ajax로 처리하기
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def login(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def suggest(request):
    if request.method == "POST":
        form = Suggest_Form(request.POST)
        if form.is_valid():
            suggest_data = form.save(commit=False)
            suggest_data.save()
            return redirect('/')
    else:
        form = Suggest_Form()
    return render(request, 'bcms/suggest.html', {'form':form},)