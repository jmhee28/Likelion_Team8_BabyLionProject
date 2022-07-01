from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User
from .models import Blog
from .models import CategoryTree
from .models import Comment
from .models import Individual_info

class UserAdmin(BaseUserAdmin):
    # 관리자 화면에 보여질 칼럼 지정
    list_display = ('username','name','email','create_dt','last_login','is_admin','is_staff', 'university', 'major', 'phone_number', 'address')
    search_fields = ('username', 'name','email')
    readonly_fields = ('id', 'create_dt', 'last_login')

    list_filter = ('is_admin',)
    ordering = ()
    fieldsets = ()
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(Blog)
admin.site.register(CategoryTree)
admin.site.register(Comment)
admin.site.register(Individual_info)