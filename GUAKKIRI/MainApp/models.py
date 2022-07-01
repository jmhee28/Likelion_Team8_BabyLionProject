import email
from django.db import models
from django.contrib.auth.models import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    category1 = models.CharField(max_length=100, null=True)
    category2 = models.CharField(max_length=100, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class CategoryTree(models.Model): 
    category1 = models.CharField(max_length=100)
    category2 = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category2

class Comment(models.Model): 
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Individual_info(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    posting_num=models.IntegerField(blank=True,default=0 )
    photo = models.ImageField(blank=True, null=True, upload_to='profile_photo')

    def __str__(self):
        return self.user.username

class UserManager(BaseUserManager):
    # 일반 user 생성, username 이 userID를 의미함
    def create_user(self,email,username, name,university, major, address, phone_number,password=None, ):
        if not username:
            raise ValueError("Users must have an userID.")
        if not name:
            raise ValueError("Users must have an name.")
        if not email:
            raise ValueError("Users must have an email address.")
        if not  university:
            msg = 'Please Verify Your university'
            raise ValueError(msg)    
        if not  major:
            msg = 'Please Verify Your major'
            raise ValueError(msg) 
        if not address:
            msg = 'Please Verify Your address'
            raise ValueError(msg) 
        if not phone_number:
            msg = 'Please Verify Your phone_number'
            raise ValueError(msg)     
        user = self.model(
            username = username,
            name = name,
            email = self.normalize_email(email),
            university = university,
            major = major,
            address = address,
            phone_number = phone_number

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 User 생성
    def create_superuser(self,email,username, name,university, major, address, phone_number,password ):
        user = self.create_user(
           username = username,
            name = name,
            email = self.normalize_email(email),
            university = university,
            major = major,
            address = address,
            phone_number = phone_number
            
        )
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username    = models.CharField(max_length=30, unique=True)
    name        = models.CharField(max_length=40, null=False, blank=False)
    email       = models.EmailField(verbose_name='email', max_length=60, unique=True)
    create_dt = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    university = models.CharField(verbose_name='대학명', max_length=100)
    major = models.CharField(verbose_name='전공', max_length=100)
    address = models.CharField(verbose_name='주소', max_length=100)
    phone_number = models.CharField(verbose_name='핸드폰 번호', max_length=100)
    # is_superuser = models.BooleanField(default=False)

    object = UserManager()  # 헬퍼 클래스 사용

    USERNAME_FIELD = 'email'  # 로그인 ID로 사용할 필드
    REQUIRED_FIELDS = ['username','name','university', 'major', 'address','phone_number'] # 필수 작성 필드

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin