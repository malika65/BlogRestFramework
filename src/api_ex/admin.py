from django.contrib import admin
from .models import Post, Tag,News

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
# admin.site.register(News)



@admin.register(News)
class QuillPostAdmin(admin.ModelAdmin):
    pass