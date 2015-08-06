from django.contrib import admin
from news.models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}


class NoteToPostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'author')


admin.site.register(News, NewsAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(NoteToPost, NoteToPostAdmin)
