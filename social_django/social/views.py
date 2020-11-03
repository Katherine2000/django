from django.shortcuts import render, redirect
from .models import *

from django.contrib import messages
# Create your views here.
def feed(request):
	posts = Post.objects.all()

	context = { 'posts' : posts}
	return render(request, 'social/feed.html', context)

def profile(request):
	return render(request, 'social/profile.html')