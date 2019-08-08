from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.utils import timezone
from blogging.models import Post, Category
from blogging.forms import PostForm, PublishForm, ListForm


def list_view(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("/login")

        form = PublishForm(request.POST)

        if form.is_valid():
            post = Post.objects.get(id=form.cleaned_data["post_id"])

            if request.user == post.author:
                post.published_date = None
                post.save()
                return redirect("/")
        else:
            print(form.errors)

    form = PublishForm()

    published = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )

    return render(request, "blogging/list.html", {"posts": published})


def unpublished_view(request):
    """
    Returns a form displaying all unpublished posts for the current user.
    Each post includes a publish button that publishes the post with the current time
    """

    if not request.user.is_authenticated:
        return redirect("/login")

    if request.method == "POST":
        form = PublishForm(request.POST)

        if form.is_valid():
            post = Post.objects.get(id=form.cleaned_data["post_id"])
            if request.user == post.author:
                post.published_date = timezone.now()
                post.save()
                return redirect("/unpublished/")
        else:
            print(form.errors)
            return redirect("/")

    unpublished = (
        Post.objects.exclude(published_date__isnull=False)
        .filter(author=request.user)
        .order_by("-created_date")
    )

    return render(request, "blogging/unpublished.html", {"posts": unpublished})


def add_post_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                new_post = Post()
                new_post.title = form.cleaned_data["title"]
                new_post.text = form.cleaned_data["text"]
                new_post.author = request.user

                if form.cleaned_data["publish"]:
                    new_post.published_date = timezone.now()

                new_post.save()

                category = Category.objects.filter(
                    name=request.POST.getlist("selected_category")[0]
                )
                new_post.categories.set(category)

                return redirect("/")
        else:
            form = PostForm()
            return render(request, "blogging/post.html", {"form": form})
    else:
        return redirect("/login")


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {"post": post}
    return render(request, "blogging/detail.html", context)


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"

    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])

    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])

    return HttpResponse(body, content_type="text/plain")
