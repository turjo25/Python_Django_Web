from django.contrib import admin
from .models import Category, Post,MenuList,UserPermissions
# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(MenuList)
admin.site.register(UserPermissions)