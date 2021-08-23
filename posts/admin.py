from django.contrib import admin
from .models import News

# Register your models here.

class AdminNews(admin.ModelAdmin):
    list_display = ['heading_one']
    list_filter = ['heading_one']

admin.site.register(News,AdminNews)

# admin.site.register(News)
