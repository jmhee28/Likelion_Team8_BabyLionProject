from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    return render(request, 'index.html')

def singlepost(request):
    return render(request, 'single-post.html')

def category(request):
    return render(request, 'category.html')

def create(request):
    return render(request, 'create.html')

def login(request):
    return render(request, 'login.html')

def searchresult(request):
    return render(request, 'search-result.html')

def write(request):
    return render(request, 'write.html')

def about(request):
    return render(request, 'about.html')




