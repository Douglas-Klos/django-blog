from django.forms import ModelForm, BooleanField, DecimalField
from django.db.utils import OperationalError, ProgrammingError
from blogging.models import Post, Category


class PostForm(ModelForm):

    publish = BooleanField(initial=False, required=False)

    # The try block is so migrate doesn't crash on a fresh database
    try:
        categories = [category for category in Category.objects.all()]
    except (OperationalError, ProgrammingError):
        pass

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
