from django.contrib import admin
from .models import Post
class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'

admin.site.register(Post)
