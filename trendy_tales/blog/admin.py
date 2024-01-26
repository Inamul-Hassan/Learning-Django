from django.contrib import admin

from .models import Posts, Author, Tag

# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ["title", "author", "date"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(Author)
admin.site.register(Tag)
