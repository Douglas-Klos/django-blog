from django.forms import ModelForm, BooleanField, DecimalField
from blogging.models import Post, Category


class PostForm(ModelForm):

    publish = BooleanField(initial=False, required=False)
    categories = [category for category in Category.objects.all()]

    class Meta:
        model = Post
        fields = ["title", "text"]


class PublishForm(ModelForm):
    post_id = DecimalField()

    class Meta:
        model = Post
        fields = []


class ListForm(ModelForm):
    post_id = DecimalField()

    class Meta:
        model = Post
        fields = []
