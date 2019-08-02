from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    # max_num = 2


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ]
    # fields = ['title', 'text', 'author', 'published_date', ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts", )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
