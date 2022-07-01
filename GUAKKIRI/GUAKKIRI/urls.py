from django.contrib import admin
from django.urls import path, include
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('home/', views.home, name ='home'),
    path('singlepost/', views.singlepost, name ='singlepost'),
    path('singlepost/<int:post_id>', views.singlepost, name ='singlepost'),
    path('create_comment/', views.create_comment, name ='create_comment'),
    path('create_comment/<int:post_id>', views.create_comment, name ='create_comment'),

    path('category/', views.category, name ='category'),
    path('category/<field>', views.category, name ='category'),

    path('create/', views.create, name ='create'),
    
    
    path('common/', include('common.urls')),
    path('login/', views.login, name ='login'),


    path('searchresult/', views.searchresult, name ='searchresult'),
    path('write/', views.write, name ='write'),
    path('about/', views.about, name ='about'),
    path('profilesettings/', views.profilesettings, name ='profilesettings'),
    path('showprofile/', views.showprofile, name ='showprofile'),
 

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)