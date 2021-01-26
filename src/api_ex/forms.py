from django import forms

from .models import Post, Tag

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