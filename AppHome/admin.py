from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','publish_time','status','category']
    list_filter = ['status','created_time','publish_time']
    prepopulated_fields = {'slug' : ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title']
    ordering = ['title',]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']