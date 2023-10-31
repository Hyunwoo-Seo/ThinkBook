from django import forms
from .models import Post, Reply


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성

class ReplyForm(forms.ModelForm):
    #text = forms.TextInput(label = '댓글')

    class Meta:
        model = Reply
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = "댓글"
