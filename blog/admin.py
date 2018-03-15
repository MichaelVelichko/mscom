from django.contrib import admin
from .models import Post
from metatags.admin import MetaTagInline
# Register your models here.
admin.site.register(Post)


class CustomModelAdmin(admin.ModelAdmin):
    inlines = (MetaTagInline,)

