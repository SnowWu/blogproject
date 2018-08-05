from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.
class PostAdmiin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
admin.site.register(Post, PostAdmiin)
admin.site.register(Category)
admin.site.register(Tag)