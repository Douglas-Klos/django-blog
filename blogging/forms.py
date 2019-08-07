from django.forms import ModelForm, BooleanField
from blogging.models import Post, Category

class PostForm(ModelForm):

    publish = BooleanField(initial=False, required=False)
    categories = [category for category in Category.objects.all()]

    class Meta:
        model = Post
        fields = ['title', 'text']


class PublishForm(ModelForm):

    publish = BooleanField(initial=False, required=False)

    class Meta:
        model = Post
        fields = []
