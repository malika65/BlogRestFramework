from django import forms
from .models import Post, Tag,News
from django_quill.forms import QuillFormField

class QuillFieldForm(forms.Form):
    body = QuillFormField()


class QuillPostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            'title',
            'body',
        )

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body','tags',)

    # Can do without this part , this is for beauty
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple 
    )


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name', )