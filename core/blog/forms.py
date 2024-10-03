from django import forms
from .models import post , Comment , category

# Reordering Form and View


class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-4",
                "name": "title",
                "placeholder": "enter the title",
            }
        ),
        label="",
    )
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-4",
                "name": "content",
                "placeholder": "enter the title",
            }
        ),
        label="",
    )
    category = forms.ModelMultipleChoiceField(
        queryset=category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = post
        fields = ("title","content","category")




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']