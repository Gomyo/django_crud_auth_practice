from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('user',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
