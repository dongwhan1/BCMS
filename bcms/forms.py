from django import forms
from .models import Post, Comment, Map_Data, Suggest_Data

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        help_texts = {
            'author': '학번과 이름을 입력하세요'
        }
        fields = ('author', 'title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class Map_Data_Form(forms.ModelForm):
    class Meta:
        model = Map_Data
        fields = ('author', 'loc_x', 'loc_y', 'title', 'information')

class Suggest_Form(forms.ModelForm):
    class Meta:
        model = Suggest_Data
        help_texts = {
            'author': '학번과 이름을 입력하세요'
        }
        fields = ('board', 'author', 'text')