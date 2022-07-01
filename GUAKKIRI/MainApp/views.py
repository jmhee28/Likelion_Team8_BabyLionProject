from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone
from common.forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required


def home(request):
    posts=Blog.objects.all()
    fields=CategoryTree.objects.all()
    if request.user.is_authenticated:
        info=Individual_info()
        info=Individual_info.objects.filter(user=request.user)
        return render(request, 'index.html',{'fields':fields,'posts':posts,'info':info})
    else:
        return render(request, 'index.html',{'fields':fields,'posts':posts,})

def singlepost(request, post_id):       
    single_post = get_object_or_404(Blog, pk=post_id)
    post_comments = Comment.objects.filter(post=post_id)
    if post_comments:
        return render(request, 'single-post.html', {'single_post':single_post,"post_id":post_id, "post_comments":post_comments})
    else:
        return render(request, 'single-post.html', {'single_post':single_post, "post_id":post_id, })


def create_comment(request, post_id):
    post=get_object_or_404(Blog, pk=post_id)
    comment=Comment()
    comment.comment=request.POST["comment"]
    if request.user.is_authenticated:
        comment.user=request.user
    comment.date=timezone.now()
    comment.post=post
    comment.save()
    return redirect(singlepost, post_id)

        
def category(request, field):
    upperCat=CategoryTree.objects.get(category2=field)
    posts=Blog.objects.filter(category2=field)
    return render(request, 'category.html',{'posts':posts, 'upperCat':upperCat})

def create(request):
    return render(request, 'create.html')

def login(request):
    return render(request, 'login.html')

def searchresult(request):
    if request.method =='POST':
        keyword=request.POST['searchkeyword']
        results=Blog.objects.filter(body__icontains=keyword)
    return render(request, 'search-result.html',{'results':results, 'keyword':keyword})



def write(request):
    if request.method =='POST'or request.method == 'FILES':
        post=Blog()
        post.title=request.POST['title']
        post.body=request.POST['body']
        post.category1=request.POST['category1']
        post.category2=request.POST['category2']
        post.photo=request.FILES.get('photo')
        if request.user.is_authenticated:
            post.user=request.user
        post.date=timezone.now()
        post.save()
        return redirect(singlepost, post.id)

    else:
        return render(request, 'write.html')

def about(request):
    return render(request, 'about.html')

def showprofile(request):
    return render(request, 'showprofile.html')

def profilesettings(request):   
    if request.method == 'POST'or request.method == 'FILES':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            profile=request.FILES.get('photo')
            return showprofile(request,{"profile":profile})

    else:
        form = CustomUserChangeForm(instance = request.user)  
        context = {
            'form':form,

        }    
        return render(request, 'profile_settings.html',context)
       



