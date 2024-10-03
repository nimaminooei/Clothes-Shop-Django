from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import post ,Comment,category,tag


class PostAdmin(admin.ModelAdmin):
    model = post
    list_display = ("author", "title","published_date",)
    # list_filter = ("status",)
    fieldsets = (("fields", {"fields": ( "content","title","category","author","tag")}),)
    add_fieldsets = (
        (None, {"Add post": ("wide",), "fields": ("author","title","category", "content","tag")}),
    )
    search_fields = ("author", "title")
    ordering = ("published_date",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at','parent')
    list_filter = ('post', 'author','created_at','parent')
    search_fields = ('text', 'author','parent')

class categoryAdmin(admin.ModelAdmin):
    pass
class tagAdmin(admin.ModelAdmin):
    pass
admin.site.register(category, categoryAdmin)
admin.site.register(tag, tagAdmin)
admin.site.register(post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
