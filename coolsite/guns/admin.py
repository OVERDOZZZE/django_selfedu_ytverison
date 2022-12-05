from django.contrib import admin
from .models import Guns, Category
# Register your models here.


class GunsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('photo', 'cat')


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     search_fields = ('name')
#     prepopulated_fields = {"slug": ('name')}



admin.site.register(Guns, GunsAdmin)
admin.site.register(Category)
