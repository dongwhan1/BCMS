from django import forms
from .models import Post, Comment, Map_Data, Suggest_Data

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('board', 'title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class Suggest_Form(forms.ModelForm):
    class Meta:
        model = Suggest_Data
        help_texts = {
            'author': '학번과 이름을 입력하세요'
        }
        fields = ('author', 'text')