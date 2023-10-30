from django.contrib import admin
from .models import Post, Comment, Vote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'post_modified',)
    search_fields = ('slug',)
    list_filter = ('post_modified',)
    prepopulated_fields = {'slug':('body',)}
    raw_id_fields = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'is_replay')
    raw_id_fields = ('user', 'post', 'replay')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass