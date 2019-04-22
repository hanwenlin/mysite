#-*- coding:utf-8 -*-
from django.contrib import admin
from .models import BlogArticle
# Register your models here.

class BlogArticleAdmin(admin.ModelAdmin):
    # 展示字段
    list_display = ('title','author','publish','title')
    # 过滤器字段
    list_filter = ('author','publish')
    # 搜索框搜索
    search_fields = ('body','title')
    #
    raw_id_fields = ('author',)
    # 添加时间轴
    date_hierarchy = 'publish'
    ordering = ['publish','author']


admin.site.register(BlogArticle,BlogArticleAdmin)