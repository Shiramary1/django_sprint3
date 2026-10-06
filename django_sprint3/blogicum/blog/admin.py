from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)
    readonly_fields = ('created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'location',
        'pub_date',
        'is_published',
        'created_at',
    )
    list_filter = (
        'is_published',
        'category',
        'location',
        'pub_date',
    )
    search_fields = ('title', 'text', 'author__username')
    date_hierarchy = 'pub_date'
    autocomplete_fields = ('author', 'category', 'location')
    readonly_fields = ('created_at',)
    list_select_related = ('author', 'category', 'location')
