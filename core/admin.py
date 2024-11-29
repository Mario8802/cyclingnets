from django.contrib import admin
from .models import News, Page

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Показвани полета в списъка
    search_fields = ('title', 'content')  # Търсене по заглавие и съдържание
    list_filter = ('created_at',)  # Филтриране по дата
    ordering = ('-created_at',)  # Най-новите новини първи


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')  # Показвани полета за страници
    search_fields = ('title', 'content')  # Търсене по заглавие и съдържание
    prepopulated_fields = {'slug': ('title',)}  # Автоматично генериране на slug
    list_filter = ('created_at',)  # Филтриране по дата
    ordering = ('-created_at',)  # Най-новите страници първи
