# Lesson 08 Assignment Notes

Addons:

## ModelForms

I created a model form for adding a new post outside of the admin panel.  This view
requires that the user be logged in (and redirects them to login if they're not) before
presenting the page for adding a new post.  Input boxes for the title, content, a checkbox
for publish, and a dropdown of categories are presented to the user.  The current user
is assumed to be the author.


# Lesson 07 Assignment Notes

After Joe mentioned some people had their git repo setup incorrectly for the django blog assignment I moved the .git folder up into the
mysite folder and readded the files.  Git recognized this as files having been moved.  From there I recloned the repo and setup a new
database to ensure that the project was still functioning after the move.  No problems were detected.  Further, while working through
lesson 07 I had made a couple of changes to the database, adding a new foreignkey, and then later removing it.  These migrations were
removed in the most recent commit as they are not needed.

Otherwise this was a fairly straight forward assignment.  Really it came down to just six new lines of code plus two modified lines.
I believe the only changes were made to the blogging/admin.py file.

## blogging/admin.py
```
from django.contrib import admin
from blogging.models import Post, Category

# New Lines
class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts", )

# Modified Lines
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
```
