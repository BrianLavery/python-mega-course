from django.contrib import admin
from .models import Post

# Change how info is displayed by default
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')

# Register your models here.
admin.site.register(Post, PostAdmin)