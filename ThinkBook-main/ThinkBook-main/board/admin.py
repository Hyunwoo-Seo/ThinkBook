from django.contrib import admin
from .models import Post, Tag, Reply

admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Tag)