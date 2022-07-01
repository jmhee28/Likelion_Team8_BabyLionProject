from django.shortcuts import render

# Create your views here.
from datetime import timedelta

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from common.decorators import keep_login
from common.forms import UserForm
from MainApp.views import home
from django.contrib.auth import login, authenticate, logout

from django.utils.decorators import method_decorator


def signup(request):
    """
    계정 생성
    """ 
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['password1']
            email = authenticate(username= email, password=raw_password)
            login(request, email)
            return home(request)    
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})


class CustomLoginView(LoginView):
    template_name = 'common/login.html'
        
    @method_decorator(keep_login)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

