from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'text', 'reader_role')
