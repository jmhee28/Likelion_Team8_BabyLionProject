from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('home/', views.home, name ='home'),
    path('singlepost/', views.singlepost, name ='singlepost'),
    path('category/', views.category, name ='category'),
    path('create/', views.create, name ='create'),
    path('login/', views.login, name ='login'),
    path('searchresult/', views.searchresult, name ='searchresult'),
    path('write/', views.write, name ='write'),
    path('about/', views.about, name ='about'),

]
