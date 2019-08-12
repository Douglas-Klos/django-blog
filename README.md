# Lesson 08 Assignment Notes

I liked this weeks assignment, it felt like actually putting work in and creating a site
instead of just following instructions.

Blog is live at: py230-ubtuntu02004019.westus.cloudapp.azure.com

## Google Login

I don't have an active Facebook account so I implemented the 3rd party login using
google's services.  Redirects to / after logging in.

## RSS Feed

I don't have much experience working with RSS feeds, but I believe that I have this
functioning.  It will load into an RSS feed reader, and show a list of new posts.
These can then be clicked on, which loads the appropriate detailed view page for that
post.

## ModelForms

Without Model Forms this whole website is basically useless, you don't want to have
to go to the backend to add posts everytime on a blog.

So I created a model form for adding a new post outside of the admin panel.  This view
requires that the user be logged in (and redirects them to login if they're not) before
presenting the page for adding a new post.  Input boxes for the title, content, a
checkbox for publish, and a dropdown of categories are presented to the user.  The
current user is assumed to be the author.

A new view called 'unpublished' was added.  This page displays all of the users current
unpublished posts, incluing a publish button for each post.  If the publish button is
clicked for a specific post, it is published with the current time and the user is
returned the unpublished posts view.

The main list display view has been updated with an 'unpublish' button that is presented
to the user on each of their posts.  This allows the user to unpublish the post.
Unpublished posts can be republished from the unpublished view.


### Issues

One hang-up I'm having, I'm able to store time information in UTC, but when displaying
it back to the user in templates, I can't get it to display in localtime.  I've tried
various things such as:
```
{% load tz %}
{{ post.published_date|localtime }}
```
It appears this is more complicated than just a form setting, that it needs javascript
to get the users current timezone then and render it appropriately.  I'm open to
suggestions.



# Lesson 07 Assignment Notes

After Joe mentioned some people had their git repo setup incorrectly for the django blog
assignment I moved the .git folder up into the mysite folder and readded the files.  Git
recognized this as files having been moved.  From there I recloned the repo and setup a
new database to ensure that the project was still functioning after the move.  No
problems were detected.  Further, while working through lesson 07 I had made a couple of
changes to the database, adding a new foreignkey, and then later removing it.  These
migrations were removed in the most recent commit as they are not needed.

Otherwise this was a fairly straight forward assignment.  Really it came down to just
six new lines of code plus two modified lines.  I believe the only changes were made to
the blogging/admin.py file.

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
