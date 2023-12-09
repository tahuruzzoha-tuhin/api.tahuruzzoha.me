from django.contrib import admin
from main.models import BaseBlogModel
# Register your models here.

class BaseBlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']


admin.site.register(BaseBlogModel, BaseBlogModelAdmin)