from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.utils import timezone
from blogging.models import Post, Category
from blogging.forms import PostForm, PublishForm
from datetime import datetime


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"

    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])

    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])

    return HttpResponse(body, content_type="text/plain")


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by("-published_date")
    context = {"posts": posts}
    return render(request, "blogging/list.html", context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {"post": post}
    return render(request, "blogging/detail.html", context)


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
                    new_post.published_date = timezone.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

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


def unpublished_view(request):
        
    if not request.user.is_authenticated:
        return redirect('/login')
    
    if request.method == "POST":
        form = PublishForm(request.POST)        
        if form.is_valid():
            print("valid form")
            return redirect('/unpublished/')
        else:
            print(form.errors)
        
    form = PublishForm()

    unpublished = (
        Post.objects.exclude(published_date__isnull=False)
        .filter(author=request.user)
        .order_by("-created_date")
    )

    return render(request, 'blogging/unpublished.html', {'posts': unpublished})

    # if not request.user.is_authenticated:
    #     return redirect("/login")

    # if request.method == "POST":
    #     form = PublishForm(request.POST)
    #     if form.is_valid():
    #         print("Valid Form")
    #         return redirect("unpublished/")
    #     else:
    #         print("Invalid Form")

    # else:
    #     unpublished = (
    #         Post.objects.exclude(published_date__isnull=False)
    #         .filter(author=request.user)
    #         .order_by("-created_date")
    #     )
    #     form = PublishForm()
    #     context = {"posts": unpublished}
    #     return render(request, "blogging/unpublished.html", context)
