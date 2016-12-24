from django.contrib import admin
from .models import Post
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js
from django.contrib.admin.templatetags.admin_list import date_hierarchy

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)
# Register your models here.
