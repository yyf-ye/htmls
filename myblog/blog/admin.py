from django.contrib import admin

# Register your models here.
from .models import Post,Category,Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'createtime', 'modifytime', 'category','author']
    fields = ['title', 'body', 'excerpt', 'category', 'tag']

    def save_model(self, request, obj, form, change):
       obj.author = request.user
       super().save_model(request, obj, form, change)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)